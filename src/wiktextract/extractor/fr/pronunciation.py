import re

from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import LEVEL_KIND_FLAGS, TemplateNode

from ...page import clean_node
from ...wxr_context import WiktextractContext
from ..share import set_sound_file_url_fields
from .models import Sound, WordEntry
from .tags import translate_raw_tags


def extract_pronunciation(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    level_node: WikiNode,
    base_data: WordEntry,
) -> None:
    sounds_list = []
    lang_code = base_data.lang_code
    for node in level_node.find_child(
        NodeKind.LIST | LEVEL_KIND_FLAGS | NodeKind.TEMPLATE
    ):
        if node.kind == NodeKind.LIST:
            for list_item_node in node.find_child(NodeKind.LIST_ITEM):
                sounds_list.extend(
                    process_pron_list_item(wxr, list_item_node, [], lang_code)
                )
        elif isinstance(node, TemplateNode):
            if node.template_name in ["cmn-pron", "zh-cmn-pron"]:
                sounds_list.extend(process_cmn_pron_template(wxr, node))
        elif node.kind in LEVEL_KIND_FLAGS:
            from .page import parse_section

            parse_section(wxr, page_data, base_data, node)

    if len(sounds_list) == 0:
        return
    if len(page_data) == 0:
        page_data.append(base_data.model_copy(deep=True))

    if level_node.kind == NodeKind.LEVEL3:
        # Add extracted sound data to all sense dictionaries that have the same
        # language code when the prononciation subtitle is a level 3 title node.
        # Otherwise only add to the last one.
        for sense_data in page_data:
            if sense_data.lang_code == lang_code:
                sense_data.sounds.extend(sounds_list)
    else:
        page_data[-1].sounds.extend(sounds_list)


PRON_TEMPLATES = frozenset(
    [
        "pron",  # redirect to "prononciation"
        "prononciation",
        "//",  # redirect to "prononciation"
        "phon",  # redirect to "prononciation"
        "pron-recons",  # use "pron"
        "prononciation reconstruite",  # redirect to "pron-recons"
        "pron recons",  # redirect to "pron-recons"
        "lang",  # used in template "cmn-pron", which expands to list of Pinyin
    ]
)


def process_pron_list_item(
    wxr: WiktextractContext,
    list_item_node: WikiNode,
    parent_raw_tags: list[str],
    lang_code: str,
) -> list[Sound]:
    current_raw_tags = parent_raw_tags[:]
    sounds_list = []
    pron_key = "zh_pron" if lang_code == "zh" else "ipa"
    after_colon = False
    for child_index, list_item_child in enumerate(list_item_node.children):
        if isinstance(list_item_child, TemplateNode):
            sounds_list.extend(
                process_sound_list_item_templates(
                    wxr, list_item_child, current_raw_tags, after_colon
                )
            )
        elif isinstance(list_item_child, WikiNode):
            if list_item_child.kind == NodeKind.BOLD:
                current_raw_tags.append(clean_node(wxr, None, list_item_child))
            elif list_item_child.kind == NodeKind.LINK:
                for span_tag in list_item_child.find_html_recursively("span"):
                    sound = Sound(
                        ipa=clean_node(wxr, None, span_tag),
                        raw_tags=current_raw_tags[:],
                    )
                    translate_raw_tags(sound)
                    sounds_list.append(sound)
        elif isinstance(list_item_child, str):
            if ":" in list_item_child:
                after_colon = True
                pron_text = list_item_child[
                    list_item_child.find(":") + 1 :
                ].strip()
                if len(pron_text) > 0:
                    sound = Sound(raw_tags=current_raw_tags[:])
                    setattr(sound, pron_key, pron_text)
                    translate_raw_tags(sound)
                    sounds_list.append(sound)

    for nest_list_item in list_item_node.find_child_recursively(
        NodeKind.LIST_ITEM
    ):
        sounds_list.extend(
            process_pron_list_item(
                wxr, nest_list_item, current_raw_tags, lang_code
            )
        )

    return sounds_list


def process_sound_list_item_templates(
    wxr: WiktextractContext,
    template_node: TemplateNode,
    raw_tags: list[str],
    after_colon: bool,
) -> list[Sound]:
    if template_node.template_name in PRON_TEMPLATES:
        return process_pron_template(wxr, template_node, raw_tags)
    elif template_node.template_name in {
        "écouter",
        "audio",
        "pron-rég",
    }:
        return [process_ecouter_template(wxr, template_node, raw_tags)]
    elif template_node.template_name == "pron-rimes":
        return [process_pron_rimes_template(wxr, template_node, raw_tags)]
    elif not after_colon:  # location
        raw_tag = clean_node(wxr, None, template_node)
        raw_tags.append(raw_tag)

    return []


def process_pron_template(
    wxr: WiktextractContext, template_node: TemplateNode, raw_tags: list[str]
) -> list[Sound]:
    if (
        template_node.template_name in PRON_TEMPLATES
        and isinstance(template_node.template_parameters.get(1, ""), str)
        and len(template_node.template_parameters.get(1, "")) == 0
    ):
        # some pages don't pass IPA parameter to the "pron" template
        # and expand to an edit link for adding the missing data.
        return []
    sounds_list = []
    pron_texts = clean_node(wxr, None, template_node)
    if len(pron_texts) > 0:
        use_key = "zh_pron" if template_node.template_name == "lang" else "ipa"
        prons = set()
        for pron_text in re.split(",|，", pron_texts):
            pron_text = pron_text.strip()
            if len(pron_text) > 0 and pron_text not in prons:
                prons.add(pron_text)
                sound = Sound(raw_tags=raw_tags[:])
                setattr(sound, use_key, pron_text)
                translate_raw_tags(sound)
                sounds_list.append(sound)
    return sounds_list


def process_ecouter_template(
    wxr: WiktextractContext,
    template_node: TemplateNode,
    raw_tags: list[str],
) -> Sound:
    # sound file template: https://fr.wiktionary.org/wiki/Modèle:écouter
    sound = Sound()
    location = clean_node(
        wxr, None, template_node.template_parameters.get(1, "")
    )
    if location.startswith("(") and location.endswith(")"):
        location = location.strip("()")
    ipa = clean_node(
        wxr,
        None,
        template_node.template_parameters.get(
            2, template_node.template_parameters.get("pron", "")
        ),
    )
    audio_file = clean_node(
        wxr, None, template_node.template_parameters.get("audio", "")
    )
    if len(raw_tags) > 0:
        sound.raw_tags = raw_tags[:]
    if len(location) > 0:
        sound.raw_tags.append(location)
    if len(ipa) > 0:
        sound.ipa = ipa
    if len(audio_file) > 0:
        set_sound_file_url_fields(wxr, audio_file, sound)
    translate_raw_tags(sound)
    return sound


def is_ipa_text(text: str) -> bool:
    # check if the text is IPA, used for inflection table cell text
    if text.startswith("\\") and text.endswith("\\"):
        return True
    if text.startswith("ou ") and text.endswith("\\"):
        # some inflection table template like "en-nom-rég" might have a second
        # ipa text in a new line
        return True
    return False


def process_pron_rimes_template(
    wxr: WiktextractContext,
    template_node: TemplateNode,
    raw_tags: list[str],
) -> Sound:
    # https://fr.wiktionary.org/wiki/Modèle:pron-rimes
    sound = Sound()
    expanded_node = wxr.wtp.parse(
        wxr.wtp.node_to_wikitext(template_node), expand_all=True
    )
    for index, span_tag in enumerate(
        expanded_node.find_html_recursively("span")
    ):
        span_text = clean_node(wxr, None, span_tag)
        if index == 0:
            sound.ipa = span_text
        elif index == 1:
            sound.rhymes = span_text
    if len(raw_tags) > 0:
        sound.raw_tags = raw_tags[:]
    translate_raw_tags(sound)
    return sound


def process_cmn_pron_template(
    wxr: WiktextractContext, template_node: TemplateNode
) -> list[Sound]:
    # https://fr.wiktionary.org/wiki/Modèle:cmn-pron
    sounds_list = []
    expanded_node = wxr.wtp.parse(
        wxr.wtp.node_to_wikitext(template_node),
        pre_expand=True,
        additional_expand={template_node.template_name},
    )
    for list_node in expanded_node.find_child(NodeKind.LIST):
        for list_item in list_node.find_child(NodeKind.LIST_ITEM):
            sounds_list.extend(process_pron_list_item(wxr, list_item, [], "zh"))

    return sounds_list

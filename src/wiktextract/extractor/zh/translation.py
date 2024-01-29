from typing import Optional, Union

from mediawiki_langcodes import code_to_name, name_to_code
from wikitextprocessor import NodeKind, WikiNode
from wikitextprocessor.parser import LEVEL_KIND_FLAGS, TemplateNode
from wiktextract.page import clean_node
from wiktextract.wxr_context import WiktextractContext

from .models import Translation, WordEntry


def extract_translation(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    level_node: WikiNode,
    sense: str = "",
) -> None:
    for child in level_node.find_child(NodeKind.TEMPLATE | NodeKind.LIST):
        if isinstance(child, TemplateNode):
            template_name = child.template_name.lower()
            if (
                template_name in {"trans-top", "翻譯-頂", "trans-top-also"}
                and 1 in child.template_parameters
            ):
                sense = clean_node(wxr, None, child.template_parameters.get(1))
            elif template_name == "see translation subpage":
                translation_subpage(wxr, page_data, child.template_parameters)
        else:
            for list_item in child.find_child_recursively(NodeKind.LIST_ITEM):
                process_translation_list_item(
                    wxr,
                    page_data,
                    list_item,
                    sense,
                )


def process_translation_list_item(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    list_item: WikiNode,
    sense: str,
) -> None:
    tr_data = Translation(word="", sense=sense)

    for child in list_item.children:
        if isinstance(child, str) and child.strip().endswith(("：", ":")):
            tr_data.lang = clean_node(wxr, None, child).strip("：:")
            tr_data.lang_code = name_to_code(tr_data.lang, "zh")
        elif isinstance(child, TemplateNode):
            template_name = child.template_name
            if template_name in {
                "t",
                "t+",
                "tt",
                "tt+",
                "t-check",
                "t+check",
                "t-needed",
            }:
                if len(tr_data.word) > 0:
                    page_data[-1].translations.append(
                        tr_data.model_copy(deep=True)
                    )
                    tr_data = Translation(
                        word="",
                        lang=tr_data.lang,
                        lang_code=tr_data.lang_code,
                        sense=sense,
                    )
                if tr_data.lang_code == "":
                    tr_data.lang_code = child.template_parameters[1]
                if tr_data.lang == "":
                    tr_data.lang = code_to_name(tr_data.lang_code, "zh")
                tr_data.word = clean_node(
                    wxr, None, child.template_parameters[2]
                )
                tr_data.roman = clean_node(
                    wxr, None, child.template_parameters.get("tr", "")
                )
                tr_data.alt = clean_node(
                    wxr, None, child.template_parameters.get("alt", "")
                )
                tr_data.lit = clean_node(
                    wxr, None, child.template_parameters.get("lit", "")
                )
                # find gender tags
                expanded_template = wxr.wtp.parse(
                    wxr.wtp.node_to_wikitext(child), expand_all=True
                )
                for span_node in expanded_template.find_html("span"):
                    class_str = span_node.attrs.get("class", "")
                    if "gender" in class_str:
                        for abbr_tag in span_node.find_html("abbr"):
                            if len(abbr_tag.attrs.get("title")) > 0:
                                tr_data.tags.append(
                                    clean_node(
                                        wxr, None, abbr_tag.attrs.get("title")
                                    )
                                )
                    elif tr_data.roman == "" and class_str.startswith("tr "):
                        tr_data.roman = clean_node(wxr, None, span_node)
            elif template_name == "multitrans":
                multitrans = wxr.wtp.parse(
                    child.template_parameter.get("data", "")
                )
                extract_translation(wxr, page_data, multitrans, sense)
            else:
                # qualifier template
                tag = clean_node(wxr, None, child)
                if len(tag) > 0:
                    tr_data.tags.append(tag.strip("()"))
        elif isinstance(child, WikiNode) and child.kind == NodeKind.LINK:
            if len(tr_data.word) > 0:
                page_data[-1].translations.append(tr_data.model_copy(deep=True))
                tr_data = Translation(
                    word="",
                    lang=tr_data.lang,
                    lang_code=tr_data.lang_code,
                    sense=sense,
                )
            tr_data.word = clean_node(wxr, None, child)

    if len(tr_data.word) > 0:
        page_data[-1].translations.append(tr_data.model_copy(deep=True))


def translation_subpage(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    template_args: dict[str, str],
) -> None:
    from .page import ADDITIONAL_EXPAND_TEMPLATES

    page_title = wxr.wtp.title
    target_section = None
    if len(template_args) > 0:
        target_section = template_args.get(1)
    if len(template_args) > 1:
        page_title = template_args.get(2)

    translation_subpage_title = f"{page_title}/翻譯"
    subpage = wxr.wtp.get_page(translation_subpage_title)
    if subpage is None:
        return

    root = wxr.wtp.parse(
        subpage.body,
        pre_expand=True,
        additional_expand=ADDITIONAL_EXPAND_TEMPLATES,
    )
    target_section_node = (
        root
        if target_section is None
        else find_subpage_section(wxr, root, target_section)
    )
    translation_node = find_subpage_section(
        wxr, target_section_node, wxr.config.OTHER_SUBTITLES["translations"]
    )
    if translation_node is not None:
        extract_translation(wxr, page_data, translation_node)


def find_subpage_section(
    wxr: WiktextractContext,
    node: Union[WikiNode, str],
    target_section: Union[str, list[str]],
) -> Optional[WikiNode]:
    if isinstance(node, WikiNode):
        if node.kind in LEVEL_KIND_FLAGS:
            section_title = clean_node(wxr, None, node.largs)
            if (
                isinstance(target_section, str)
                and section_title == target_section
            ):
                return node
            if (
                isinstance(target_section, list)
                and section_title in target_section
            ):
                return node

        for child in node.children:
            returned_node = find_subpage_section(wxr, child, target_section)
            if returned_node is not None:
                return returned_node
    return None

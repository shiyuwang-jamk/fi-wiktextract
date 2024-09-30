import re
from typing import Any

from mediawiki_langcodes import name_to_code
from wikitextprocessor.parser import LEVEL_KIND_FLAGS, LevelNode, NodeKind

from ...page import clean_node
from ...wxr_context import WiktextractContext
from .models import Sense, WordEntry
from .pos import extract_pos_section
from .section_titles import POS_DATA

PANEL_TEMPLATES = set()
PANEL_PREFIXES = set()
ADDITIONAL_EXPAND_TEMPLATES = set()


def parse_section(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    base_data: WordEntry,
    level_node: LevelNode,
) -> None:
    title_text = clean_node(wxr, None, level_node.largs)
    title_text = re.sub(r"\s*\d+$", "", title_text)
    if title_text in POS_DATA:
        extract_pos_section(wxr, page_data, base_data, level_node, title_text)

    for next_level in level_node.find_child(LEVEL_KIND_FLAGS):
        parse_section(wxr, page_data, base_data, next_level)


def parse_language_section(
    wxr: WiktextractContext, page_data: list[WordEntry], level2_node: LevelNode
) -> None:
    lang_name = clean_node(wxr, None, level2_node.largs)
    lang_code = name_to_code(lang_name, "ko")
    if lang_code == "":
        lang_code = "unknown"
    if (
        wxr.config.capture_language_codes is not None
        and lang_code not in wxr.config.capture_language_codes
    ):
        return
    wxr.wtp.start_section(lang_name)
    base_data = WordEntry(
        word=wxr.wtp.title,
        lang_code=lang_code,
        lang=lang_name,
        pos="unknown",
    )
    for level3_node in level2_node.find_child(NodeKind.LEVEL3):
        parse_section(wxr, page_data, base_data, level3_node)

    # no POS section
    if not level2_node.contain_node(NodeKind.LEVEL3):
        extract_pos_section(wxr, page_data, base_data, level2_node, "")


def parse_page(
    wxr: WiktextractContext, page_title: str, page_text: str
) -> list[dict[str, Any]]:
    # page layout
    # https://ko.wiktionary.org/wiki/위키낱말사전:문서_양식
    # https://ko.wiktionary.org/wiki/위키낱말사전:한국어_편집부
    wxr.wtp.start_page(page_title)
    tree = wxr.wtp.parse(page_text)
    page_data: list[WordEntry] = []
    for level2_node in tree.find_child(NodeKind.LEVEL2):
        parse_language_section(wxr, page_data, level2_node)

    for data in page_data:
        if len(data.senses) == 0:
            data.senses.append(Sense(tags=["no-gloss"]))
    return [m.model_dump(exclude_defaults=True) for m in page_data]

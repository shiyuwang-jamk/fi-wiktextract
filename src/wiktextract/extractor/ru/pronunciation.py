from wikitextprocessor.parser import LevelNode

from wiktextract.extractor.ru.models import WordEntry
from wiktextract.wxr_context import WiktextractContext


def extract_pronunciation(
    wxr: WiktextractContext,
    page_data: list[WordEntry],
    level_node: LevelNode,
):
    pass

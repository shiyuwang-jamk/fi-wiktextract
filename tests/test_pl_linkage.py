from unittest import TestCase

from wikitextprocessor import Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.pl.linkage import extract_linkage_section
from wiktextract.extractor.pl.models import Linkage, Sense, WordEntry
from wiktextract.wxr_context import WiktextractContext


class TestPlLinkage(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="pl"),
            WiktionaryConfig(
                dump_file_lang_code="pl",
                capture_language_codes=None,
            ),
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()

    def test_pies(self):
        self.wxr.wtp.start_page("pies")
        self.wxr.wtp.add_page("Szablon:neutr", 10, "neutr.")

        root = self.wxr.wtp.parse(""": (1.1) [[czworonożny przyjaciel]]
: (2.1) [[pała]]; {{neutr}} [[policjant]]""")
        page_data = [
            WordEntry(
                word="pies",
                lang="język polski",
                lang_code="pl",
                pos="noun",
                senses=[Sense(sense_index="1.1")],
            ),
            WordEntry(
                word="pies",
                lang="język polski",
                lang_code="pl",
                pos="noun",
                senses=[Sense(sense_index="2.1")],
            ),
        ]
        extract_linkage_section(self.wxr, page_data, root, "synonyms", "pl")
        self.assertEqual(
            page_data[0].synonyms,
            [Linkage(word="czworonożny przyjaciel", sense_index="1.1")],
        )
        self.assertEqual(
            page_data[1].synonyms,
            [
                Linkage(word="pała", sense_index="2.1"),
                Linkage(
                    word="policjant", raw_tags=["neutr."], sense_index="2.1"
                ),
            ],
        )

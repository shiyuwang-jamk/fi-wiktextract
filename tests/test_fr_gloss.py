import unittest
from collections import defaultdict
from unittest.mock import patch

from wikitextprocessor import Wtp, Page

from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.fr.gloss import extract_gloss
from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class TestFormLine(unittest.TestCase):
    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="fr"), WiktionaryConfig(dump_file_lang_code="fr")
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    @patch(
        "wikitextprocessor.Wtp.get_page",
        return_value=Page(
            "Modèle:sportifs",
            10,
            body="(Sport)[[Catégorie:Sportifs en français]]",
        ),
    )
    def test_theme_templates(self, mock_get_page):
        self.wxr.wtp.start_page("")
        root = self.wxr.wtp.parse("# {{sportifs|fr}} gloss.\n#* example")
        page_data = [defaultdict(list)]
        extract_gloss(self.wxr, page_data, root.children[0])
        self.assertEqual(
            page_data,
            [
                {
                    "senses": [
                        {
                            "glosses": ["gloss."],
                            "tags": ["Sport"],
                            "categories": ["Sportifs en français"],
                            "examples": [
                                {"text": "example", "type": "example"}
                            ],
                        }
                    ]
                }
            ],
        )

    def test_example_template(self):
        self.wxr.wtp.start_page("")
        root = self.wxr.wtp.parse(
            "# gloss.\n#* {{exemple|text|translation|roman|source=source}}"
        )
        page_data = [defaultdict(list)]
        extract_gloss(self.wxr, page_data, root.children[0])
        self.assertEqual(
            page_data,
            [
                {
                    "senses": [
                        {
                            "glosses": ["gloss."],
                            "examples": [
                                {
                                    "text": "text",
                                    "translation": "translation",
                                    "roman": "roman",
                                    "source": "source",
                                    "type": "quotation",
                                }
                            ],
                        }
                    ]
                }
            ],
        )

    @patch(
        "wikitextprocessor.Wtp.get_page",
        return_value=Page("Modèle:source", 10, body="source_title"),
    )
    def test_example_source_template(self, mock_node_to_html):
        self.wxr.wtp.start_page("")
        root = self.wxr.wtp.parse(
            "# gloss.\n#* example {{source|source_title}}"
        )
        page_data = [defaultdict(list)]
        page_data = [defaultdict(list)]
        extract_gloss(self.wxr, page_data, root.children[0])
        self.assertEqual(
            page_data,
            [
                {
                    "senses": [
                        {
                            "glosses": ["gloss."],
                            "examples": [
                                {
                                    "text": "example",
                                    "source": "source_title",
                                    "type": "quotation",
                                }
                            ],
                        }
                    ]
                }
            ],
        )

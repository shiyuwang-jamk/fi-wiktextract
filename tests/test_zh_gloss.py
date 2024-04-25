from unittest import TestCase
from unittest.mock import patch

from wikitextprocessor import NodeKind, WikiNode, Wtp
from wiktextract.config import WiktionaryConfig
from wiktextract.extractor.zh.models import Sense, WordEntry
from wiktextract.extractor.zh.page import (
    extract_gloss,
    parse_page,
    parse_section,
)
from wiktextract.thesaurus import close_thesaurus_db
from wiktextract.wxr_context import WiktextractContext


class TestGloss(TestCase):
    def setUp(self) -> None:
        self.wxr = WiktextractContext(
            Wtp(lang_code="zh"),
            WiktionaryConfig(
                capture_language_codes=None, dump_file_lang_code="zh"
            ),
        )

    def tearDown(self) -> None:
        self.wxr.wtp.close_db_conn()
        close_thesaurus_db(
            self.wxr.thesaurus_db_path, self.wxr.thesaurus_db_conn
        )

    def test_example_list(self) -> None:
        page_data = [
            WordEntry(
                lang="日語",
                lang_code="ja",
                word="可笑しい",
                pos="adj",
            )
        ]
        wikitext = """# [[好玩]]的：
## 有趣的，滑稽的，可笑的
## 奇怪的，不正常的
## 不合理的，不合邏輯的
# {{lb|ja|棄用}} [[有趣]]的：
## [[有趣]]的
## [[美味]]的
## [[漂亮]]的
## [[很好]]的，[[卓越]]的"""
        self.wxr.wtp.start_page("可笑しい")
        self.wxr.wtp.add_page("Template:lb", 10, "({{{2|}}})")
        node = self.wxr.wtp.parse(wikitext)
        extract_gloss(self.wxr, page_data, node.children[0], Sense())
        self.assertEqual(
            [s.model_dump(exclude_defaults=True) for s in page_data[0].senses],
            [
                {"glosses": ["好玩的：", "有趣的，滑稽的，可笑的"]},
                {"glosses": ["好玩的：", "奇怪的，不正常的"]},
                {"glosses": ["好玩的：", "不合理的，不合邏輯的"]},
                {
                    "glosses": ["有趣的：", "有趣的"],
                    "tags": ["obsolete"],
                },
                {
                    "glosses": ["有趣的：", "美味的"],
                    "tags": ["obsolete"],
                },
                {
                    "glosses": ["有趣的：", "漂亮的"],
                    "tags": ["obsolete"],
                },
                {
                    "glosses": ["有趣的：", "很好的，卓越的"],
                    "tags": ["obsolete"],
                },
            ],
        )

    @patch("wiktextract.extractor.zh.page.process_pos_block")
    @patch("wiktextract.extractor.zh.page.clean_node", return_value="名詞1")
    def test_pos_title_number(
        self,
        mock_clean_node,
        mock_process_pos_block,
    ) -> None:
        node = WikiNode(NodeKind.LEVEL3, 0)
        base_data = WordEntry(word="", lang_code="", lang="", pos="")
        parse_section(self.wxr, [base_data], base_data, node)
        mock_process_pos_block.assert_called()

    @patch("wiktextract.extractor.zh.page.process_pos_block")
    @patch(
        "wiktextract.extractor.zh.page.clean_node", return_value="名詞（一）"
    )
    def test_pos_title_chinese_numeral(
        self,
        mock_clean_node,
        mock_process_pos_block,
    ) -> None:
        node = WikiNode(NodeKind.LEVEL3, 0)
        base_data = WordEntry(word="", lang_code="", lang="", pos="")
        parse_section(self.wxr, [base_data], base_data, node)
        mock_process_pos_block.assert_called()

    def test_soft_redirect_zh_see(self):
        self.assertEqual(
            parse_page(
                self.wxr,
                "別个",
                """==漢語==
{{zh-see|別個}}""",
            ),
            [
                {
                    "lang": "漢語",
                    "lang_code": "zh",
                    "pos": "soft-redirect",
                    "redirects": ["別個"],
                    "senses": [{"tags": ["no-gloss"]}],
                    "word": "別个",
                }
            ],
        )

    def test_soft_redirect_ja_see(self):
        self.assertEqual(
            parse_page(
                self.wxr,
                "きさらぎ",
                """==日語==
{{ja-see|如月|二月|更衣|衣更着}}""",
            ),
            [
                {
                    "lang": "日語",
                    "lang_code": "ja",
                    "pos": "soft-redirect",
                    "redirects": ["如月", "二月", "更衣", "衣更着"],
                    "senses": [{"tags": ["no-gloss"]}],
                    "word": "きさらぎ",
                }
            ],
        )

    def test_gloss_text_only_page(self):
        # title, page wikitext, results
        test_cases = [
            [
                "paraphrase",
                "== 英语 ==\n释义；意译",
                [
                    {
                        "lang": "英语",
                        "lang_code": "en",
                        "pos": "unknown",
                        "senses": [{"glosses": ["释义；意译"]}],
                        "word": "paraphrase",
                    }
                ],
            ],
            [
                "鐵面無私",
                "==漢語==\n===釋義===\n形容[[公正]]严明，绝不因[[徇私]]或畏权而讲情面。",
                [
                    {
                        "lang": "漢語",
                        "lang_code": "zh",
                        "pos": "unknown",
                        "senses": [
                            {
                                "glosses": [
                                    "形容公正严明，绝不因徇私或畏权而讲情面。"
                                ]
                            }
                        ],
                        "word": "鐵面無私",
                    }
                ],
            ],
        ]
        for title, wikitext, results in test_cases:
            with self.subTest(title=title, wikitext=wikitext, results=results):
                self.assertEqual(
                    parse_page(self.wxr, title, wikitext),
                    results,
                )

    def test_gloss_template(self):
        self.wxr.wtp.start_page("CC")
        self.wxr.wtp.add_page("Template:n-g", 10, "{{{1|}}}")
        root = self.wxr.wtp.parse(
            "# {{n-g|[[ISO]] 3166-1 對科科斯群島（[[Cocos Islands]]）的兩字母代碼。}}"
        )
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": [
                        "ISO 3166-1 對科科斯群島（Cocos Islands）的兩字母代碼。"
                    ]
                }
            ],
        )

    def test_gloss_lable_topic(self):
        self.wxr.wtp.start_page("DC")
        self.wxr.wtp.add_page("Template:lb", 10, "(航空学)")
        root = self.wxr.wtp.parse(
            "# {{lb|en|aviation}} 道格拉斯飞行器公司的產品名稱"
        )
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": ["道格拉斯飞行器公司的產品名稱"],
                    "topics": ["aeronautics"],
                }
            ],
        )

    def test_two_label_topics(self):
        self.wxr.wtp.start_page("DOS")
        self.wxr.wtp.add_page("Template:lb", 10, "(計算機, 網路)")
        self.wxr.wtp.add_page(
            "Template:init of",
            10,
            "denial of service (“拒絕服務”)之首字母縮略詞。",
        )
        root = self.wxr.wtp.parse(
            "# {{lb|en|計算機|網路}} {{init of|en|[[denial]] of [[service]]|t=拒絕服務}}"
        )
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "form_of": [{"word": "denial of service"}],
                    "glosses": [
                        "denial of service (“拒絕服務”)之首字母縮略詞。"
                    ],
                    "topics": ["computing", "internet"],
                    "tags": ["form-of"],
                }
            ],
        )

    def test_empty_parent_gloss(self):
        self.wxr.wtp.start_page("bright")
        self.wxr.wtp.add_page("Template:lb", 10, "({{{2}}})")
        root = self.wxr.wtp.parse("""# {{lb|en|比喻义}}
## [[显然]]的，[[显眼]]的
## {{lb|en|指颜色}} [[鲜亮]]的，[[鲜艳]]的""")
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "glosses": ["显然的，显眼的"],
                    "raw_tags": ["比喻义"],
                },
                {
                    "glosses": ["鲜亮的，鲜艳的"],
                    "raw_tags": ["比喻义", "指颜色"],
                },
            ],
        )

    def test_form_of_template(self):
        self.wxr.wtp.start_page("bella")
        self.wxr.wtp.add_page(
            "Template:adj form of",
            10,
            """<small></small><span class='form-of-definition-link'><i class="Latn mention" lang="es">[[bello#西班牙語|-{bello}-]]</i></span><span class='form-of-definition use-with-mention'> 的[[Appendix:Glossary#gender|陰性]][[Appendix:Glossary#singular_number|單數]]</span>""",
        )
        root = self.wxr.wtp.parse("# {{adj form of|es|bello||f|s}}")
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "form_of": [{"word": "bello"}],
                    "glosses": ["bello 的陰性單數"],
                    "tags": ["form-of"],
                },
            ],
        )

    def test_form_of_templates(self):
        self.wxr.wtp.start_page("linda")
        self.wxr.wtp.add_page(
            "Template:inflection of",
            10,
            """{{#switch:{{{5}}}
| acc = {{{2}}} 的不定賓格單數
| dat = {{{2}}} 的不定與格單數
}}""",
        )
        page_data = parse_page(
            self.wxr,
            "linda",
            """==冰島語==
===名詞===

# {{inflection of|is|[[lindi]]||不定|acc|s}}
# {{inflection of|is|[[lindi]]||不定|dat|s}}""",
        )
        self.assertEqual(
            page_data,
            [
                {
                    "lang": "冰島語",
                    "lang_code": "is",
                    "pos": "noun",
                    "senses": [
                        {
                            "form_of": [{"word": "lindi"}],
                            "glosses": ["lindi 的不定賓格單數"],
                            "tags": ["form-of"],
                        },
                        {
                            "form_of": [{"word": "lindi"}],
                            "glosses": ["lindi 的不定與格單數"],
                            "tags": ["form-of"],
                        },
                    ],
                    "word": "linda",
                }
            ],
        )

    def test_pt_verb_form_of(self):
        self.wxr.wtp.start_page("linda")
        self.wxr.wtp.add_page(
            "Template:pt-verb form of",
            10,
            """<small></small><span class='form-of-definition-link'><i class="Latn mention" lang="pt">[[lindar#葡萄牙語|-{lindar}-]]</i></span><span class='form-of-definition use-with-mention'> 的屈折变化形式：</span>
## <span class='form-of-definition use-with-mention'>[[Appendix:Glossary#third_person|第三人稱]][[Appendix:Glossary#singular_number|單數]][[Appendix:Glossary#present_tense|現在時]][[Appendix:Glossary#indicative_mood|直陳式]]</span>
## <span class='form-of-definition use-with-mention'>[[Appendix:Glossary#second_person|第二人稱]][[Appendix:Glossary#singular_number|單數]][[Appendix:Glossary#imperative_mood|命令式]]</span>""",
        )
        root = self.wxr.wtp.parse("# {{pt-verb form of|lindar}}")
        page_data = [WordEntry(word="", lang_code="", lang="", pos="")]
        extract_gloss(self.wxr, page_data, root.children[0], Sense())
        self.assertEqual(
            page_data[0].model_dump(exclude_defaults=True)["senses"],
            [
                {
                    "form_of": [{"word": "lindar"}],
                    "glosses": [
                        "lindar 的屈折变化形式：",
                        "第三人稱單數現在時直陳式",
                    ],
                    "tags": ["form-of"],
                },
                {
                    "form_of": [{"word": "lindar"}],
                    "glosses": [
                        "lindar 的屈折变化形式：",
                        "第二人稱單數命令式",
                    ],
                    "tags": ["form-of"],
                },
            ],
        )

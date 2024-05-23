from wiktextract.config import POSSubtitleData

POS_TITLES: POSSubtitleData = {
    "不及物动词": {"pos": "verb", "tags": ["intransitive"]},
    "不及物動詞": {
        "debug": "part-of-speech Intransitive verb is proscribed",
        "pos": "verb",
        "tags": ["intransitive"],
    },
    "不定代词": {"pos": "pron"},
    "不定冠詞": {"pos": "article"},
    "不定冠词": {"pos": "article"},
    "专有名詞": {"pos": "name"},
    "专有名词": {"pos": "name"},
    "中綴": {"pos": "interfix", "tags": ["morpheme"]},
    "中缀": {"pos": "infix", "tags": ["morpheme"]},
    "习语": {"pos": "phrase", "tags": ["idiomatic"]},
    "人称代词": {"pos": "pron", "tags": ["person"]},
    "介係詞": {"pos": "prep"},
    "介系詞": {"pos": "prep"},
    "介系词": {"pos": "prep"},
    "介詞": {"pos": "prep"},
    "介詞短語": {"pos": "prep_phrase"},
    "介词": {"pos": "prep"},
    "介词短语": {"pos": "prep_phrase"},
    "代名詞": {"pos": "pron"},
    "代名词": {"pos": "pron"},
    "代詞": {"pos": "pron"},
    "代词": {"pos": "pron"},
    "俗語": {"pos": "phrase", "tags": ["idiomatic"]},
    "俗语": {"pos": "phrase", "tags": ["idiomatic"]},
    "关系代词": {"pos": "pron"},
    "冠詞": {"pos": "article"},
    "冠词": {"pos": "article"},
    "分詞": {"pos": "verb", "tags": ["participle"]},
    "分词": {"pos": "verb", "tags": ["participle"]},
    "分類詞": {"pos": "classifier"},
    "前綴": {"pos": "prefix", "tags": ["morpheme"]},
    "前綴詞": {"pos": "prefix", "tags": ["morpheme"]},
    "前缀": {"pos": "prefix", "tags": ["morpheme"]},
    "前置詞": {"pos": "prep"},
    "前置词": {"pos": "prep"},
    "副助": {"pos": "particle"},
    "副詞": {"pos": "adv"},
    "副词": {"pos": "adv"},
    "动詞": {"pos": "verb"},
    "动词": {"pos": "verb"},
    "助動詞": {"pos": "verb"},
    "助数": {"pos": "classifier", "tags": ["measure word"]},
    "助數詞": {"pos": "counter"},
    "助詞": {"pos": "particle"},
    "助词": {"pos": "particle"},
    "動名詞": {
        "debug": "part-of-speech Gerund is proscribed",
        "pos": "verb",
        "tags": ["participle", "gerund"],
    },
    "動詞": {"pos": "verb"},
    "及物动词": {"pos": "verb", "tags": ["transitive"]},
    "及物動詞": {"pos": "verb", "tags": ["transitive"]},
    "叹词": {"pos": "intj"},
    "名称": {"pos": "noun"},
    "名稱": {"pos": "noun"},
    "名詞": {"pos": "noun"},
    "名词": {"pos": "noun"},
    "后缀": {"pos": "suffix", "tags": ["morpheme"]},
    "后置词": {"pos": "postp"},
    "基数": {"pos": "num"},
    "基数词": {"pos": "num"},
    "基數": {"pos": "num"},
    "字母": {"pos": "character", "tags": ["letter"]},
    "字綴": {"pos": "affix"},
    "字面": {"debug": "typo", "pos": "character", "tags": ["letter"]},
    "定冠词": {"pos": "article"},
    "寧詞": {"debug": "typo", "pos": "noun"},
    "对应汉字": {"pos": "romanization"},
    "对应词语": {"pos": "romanization"},
    "專有名詞": {"pos": "name"},
    "小品词": {"pos": "particle"},
    "平假名": {"pos": "syllable"},
    "序數": {
        "debug": "ordinal numbers should be adjectives",
        "pos": "adj",
        "tags": ["ordinal"],
    },
    "序數詞": {"pos": "num"},
    "康熙部首": {"pos": "symbol"},
    "形容动词": {"pos": "adj_noun"},
    "形容動詞": {"pos": "adj_noun"},
    "形容詞": {"pos": "adj"},
    "形容词": {"pos": "adj"},
    "後綴": {"pos": "suffix", "tags": ["morpheme"]},
    "後置詞": {"pos": "postp"},
    "後附語素": {"pos": "suffix", "tags": ["clitic"]},
    "惯用语": {"pos": "phrase"},
    "感叹词": {"pos": "intj"},
    "感嘆詞": {"pos": "intj"},
    "感歎詞": {"pos": "intj"},
    "慣用語": {"pos": "phrase"},
    "成句": {"pos": "proverb"},
    "成語": {"pos": "phrase", "tags": ["idiomatic"]},
    "成语": {"pos": "phrase", "tags": ["idiomatic"]},
    "拼音": {"pos": "romanization"},
    "接助": {"pos": "particle"},
    "接头": {"pos": "prefix"},
    "接头詞": {"pos": "prefix"},
    "接头词": {"pos": "prefix"},
    "接尾": {"pos": "suffix"},
    "接尾詞": {"pos": "suffix"},
    "接尾词": {"pos": "suffix"},
    "提助": {"pos": "article"},
    "擬態詞": {"pos": "noun", "tags": ["ideophone"]},
    "擬聲詞": {"pos": "noun", "tags": ["onomatopoeia"]},
    "数字": {"pos": "num", "tags": ["number"]},
    "数詞": {"pos": "num", "tags": ["number"]},
    "数词": {"pos": "num", "tags": ["number"]},
    "數字": {"pos": "num", "tags": ["number"]},
    "數字符號": {"pos": "num", "tags": ["number"]},
    "數詞": {"pos": "num", "tags": ["number"]},
    "标点": {"pos": "punct", "tags": ["punctuation"]},
    "标点符号": {"pos": "punct", "tags": ["punctuation"]},
    "標點符號": {
        "debug": "part-of-speech Punctuation should be Punctuation mark",
        "pos": "punct",
        "tags": ["punctuation"],
    },
    "歇后语": {"pos": "proverb", "tags": ["xiehouyu"]},
    "歇後語": {"pos": "proverb", "tags": ["xiehouyu"]},
    "汉语拼音": {"pos": "romanization"},
    "漢語拼音": {"pos": "romanization"},
    "注音符號": {"pos": "character"},
    "漢字": {"pos": "character", "tags": ["han"]},
    "汉字": {"pos": "character", "tags": ["han"]},
    "片語": {"pos": "phrase"},
    "物主代词": {"pos": "pron"},
    "環綴": {"pos": "circumfix", "tags": ["morpheme"]},
    "短語": {"debug": "usually used in singular", "pos": "phrase"},
    "短语": {"pos": "phrase", "tags": ["idiomatic"]},
    "符号": {"pos": "symbol"},
    "符號": {"pos": "symbol"},
    "简写": {"pos": "abbrev", "tags": ["abbreviation"]},
    "縮寫": {"pos": "abbrev", "tags": ["abbreviation"]},
    "縮約形": {"pos": "contraction", "tags": ["contraction"]},
    "结合形式": {"pos": "combining_form", "tags": ["morpheme"]},
    "缩写": {
        "debug": "part-of-speech Abbreviation is proscribed",
        "pos": "abbrev",
        "tags": ["abbreviation"],
    },
    "缩约形": {"pos": "abbrev", "tags": ["abbreviation"]},
    "罗马化": {"pos": "romanization"},
    "罗马字": {"pos": "romanization"},
    "羅馬化": {"pos": "romanization"},
    "羅馬字": {"pos": "romanization"},
    "習語": {"pos": "phrase", "tags": ["idiomatic"]},
    "表語": {"pos": "adj", "tags": ["predicative"]},
    "詞綴": {"pos": "affix"},
    "諺語": {"pos": "proverb"},
    "词组": {"pos": "phrase"},
    "词缀": {"pos": "affix"},
    "语气助词": {"pos": "particle"},
    "谚语": {"pos": "proverb"},
    "连体词": {"pos": "adnominal"},
    "连词": {"pos": "conj"},
    "連詞": {"pos": "conj"},
    "連體詞": {"pos": "adnominal"},
    "部件": {"pos": "component"},
    "釋義": {
        # Means 'definition', some pages don't have POS but use this title
        "pos": "unknown"
    },
    "释义": {"pos": "unknown"},  # simplify form of "釋義"
    "解释": {"pos": "unknown"},
    "量詞": {"pos": "classifier"},
    "量词": {"pos": "classifier"},
    "間綴": {"pos": "interfix", "tags": ["morpheme"]},
    "關係詞": {"pos": "conj", "tags": ["relative"]},
    "附加符號": {"pos": "character", "tags": ["diacritic"]},
    "附著語素": {"pos": "suffix", "tags": ["morpheme"]},
    "限定詞": {"pos": "det"},
    "限定词": {"pos": "det"},
    "音節": {"pos": "syllable"},
    "音节": {"pos": "syllable"},
    "首字母縮略字": {
        "debug": "part-of-speech Initialism is proscribed",
        "pos": "abbrev",
        "tags": ["abbreviation"],
    },
    "首字母縮略詞": {"pos": "abbrev", "tags": ["abbreviation"]},
    "首字母缩略词": {"pos": "abbrev", "tags": ["abbreviation"]},
}

# map title to pydantic field
LINKAGE_TITLES: dict[str, str] = {
    "上下位關係": "hypernyms",
    "上义词": "hypernyms",
    "上位詞": "hypernyms",
    "上位語": "hypernyms",
    "上位词": "hypernyms",
    "上義詞": "hypernyms",
    "下义词": "hyponyms",
    "下位詞": "hyponyms",
    "下位語": "hyponyms",
    "下位词": "hyponyms",
    "下层词": "hyponyms",
    "下属词": "hyponyms",
    "下層概念": "derived",
    "下義詞": "hyponyms",
    "俗语": "related",
    "关联词": "related",
    "关联词条": "related",
    "其他书写系统": "synonyms",
    "其他写法": "synonyms",
    "其他变体": "synonyms",
    "其他字形": "synonyms",
    "其他字母": "synonyms",
    "其他字母系統": "synonyms",
    "其他字符系统": "synonyms",
    "其他字體": "synonyms",
    "其他寫法": "synonyms",
    "其他形式": "synonyms",
    "其他拼写方式": "synonyms",
    "其他拼写方法": "synonyms",
    "其他拼寫": "synonyms",
    "其他拼法": "synonyms",
    "其他文字": "synonyms",
    "其他文字系統": "synonyms",
    "其他書寫系統": "synonyms",
    "其他表記": "synonyms",
    "其他詞形": "synonyms",
    "其他词形": "synonyms",
    "其他译名": "synonyms",
    "其它词形": "synonyms",
    "分体词": "meronyms",
    "分體詞": "meronyms",
    "参看": "related",
    "參考詞彙": "synonyms",
    "反义符号": "antonyms",
    "反义词": "antonyms",
    "反義": "antonyms",
    "反義字": "antonyms",
    "反義詞": "antonyms",
    "另見": "related",
    "另见": "related",
    "可替代拼寫": "synonyms",
    "合寫": "related",
    "同一類別文字": "coordinate_terms",
    "同一類別詞彙": "coordinate_terms",
    "同义词": "synonyms",
    "同位詞": "coordinate_terms",
    "同意詞": "synonyms",
    "同根词": "related",
    "同类词汇": "related",
    "同級詞彙": "coordinate_terms",
    "同義字": "related",
    "同義詞": "synonyms",
    "同義語": "synonyms",
    "同類別詞彙": "coordinate_terms",
    "同類詞": "coordinate_terms",
    "同類詞彙": "coordinate_terms",
    "复合词": "derived",
    "對應詞": "coordinate_terms",
    "對等詞": "coordinate_terms",
    "局部關係詞": "meronyms",
    "延伸词": "related",
    "搭配詞": "derived",
    "整体词": "holonyms",
    "整體詞": "holonyms",
    "替代寫法": "synonyms",
    "替代形式": "synonyms",
    "杂项": "various",
    "派生": "derived",
    "派生字": "derived",
    "派生字母": "derived",
    "派生形式": "derived",
    "派生漢字": "derived",
    "派生詞": "derived",
    "派生詞彙": "derived",
    "派生詞語": "derived",
    "派生词": "derived",
    "派生词汇": "derived",
    "派生词组": "derived",
    "熟語": "related",
    "熟语": "related",
    "相似后缀": "related",
    "相似符號": "related",
    "相关后缀": "related",
    "相关形式": "related",
    "相关术语": "related",
    "相关条目": "related",
    "相关短语": "related",
    "相关词": "related",
    "相关词条": "related",
    "相关词汇": "related",
    "相关词组": "related",
    "相关词语": "related",
    "相关语": "related",
    "相關": "related",
    "相關字": "related",
    "相關派生": "related",
    "相關漢字": "related",
    "相關符號": "related",
    "相關詞": "related",
    "相關詞匯": "related",
    "相關詞彙": "related",
    "相關詞彙變格": "related",
    "相關詞會": "related",
    "相關詞條": "related",
    "相關詞語": "related",
    "相關語": "related",
    "类似中缀": "related",
    "类似后缀": "related",
    "組詞": "derived",
    "组词": "related",
    "衍生字": "derived",
    "衍生詞": "derived",
    "衍生詞彙": "derived",
    "衍生词": "derived",
    "衍生词汇": "derived",
    "複合詞": "compounds",
    "變體": "synonyms",
    "近义词": "synonyms",
    "近義詞": "synonyms",
    "近義語": "synonyms",
    "部分詞": "meronyms",
    "關聯詞": "related",
    "關聯詞彙": "related",
}

ETYMOLOGY_TITLES: frozenset[str] = frozenset(
    [
        "詞源",
        "词源",
        "典故",
        "語源",
        "语源",
        "字源",
        "詞語",
        "組成",
        "出處",
        "出处",
    ]
)

IGNORED_TITLES: frozenset[str] = frozenset(
    [
        "異序詞",
        "异序词",
        "異序词",
        "來源",
        "參考文獻",
        "参考文献",
        "參考資料",
        "參考來源",
        "参考资料",
        "参考",
        "參考",
        "參見",
        "参见",
        "參閱",
        "拓展閱讀",
        "拓展閲讀",
        "拓展阅读",
        "延伸阅读",
        "延伸閲讀",
        "延伸閱讀",
        "扩展阅读",
        "編碼",
        "编码",
        "回文",
        "回文構詞",
        "易位構詞",
        "外部鏈接",
        "外部链接",
        "外部連結",
    ]
)

INFLECTION_TITLES: frozenset[str] = frozenset(
    [
        "变格",
        "變格",
        "变位",
        "变形",
        "变位形式",
        "變位",
        "詞形變化",
        "词形变化",
        "輔音變化",
        "辅音变化",
        "語尾變化",
        "活用",
        "活用型",
        "活用形",
        "賓格",
        "屈折",
        "屈折形式",
        "曲折形式",
        "軟化變形",
    ]
)

PRONUNCIATION_TITLES: frozenset[str] = frozenset(
    ["發音", "发音", "读音", "讀音", "注音", "讀法"]
)

TRANSLATIONS_TITLES: frozenset[str] = frozenset(["翻譯", "翻译"])

DESCENDANTS_TITLES: frozenset[str] = frozenset(["派生語彙"])

NOTES_TITLES: frozenset[str] = frozenset(["使用說明"])

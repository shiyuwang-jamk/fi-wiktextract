from typing import Union

from .models import WordEntry

# https://ru.wiktionary.org/wiki/Викисловарь:Условные_сокращения
# Стиль
STYLE_TAGS: dict[str, Union[str, list[str]]] = {
    "бран.": "offensive",
    "вульг.": "vulgar",
    "высок.": "honorific",
    "гипокор.": "familiar",
    "груб.": "vulgar",
    "детск.": "childish",
    "диал.": "dialectal",
    # "дисфм.": "дисфемизм",
    "жарг.": "slang",
    "ирон.": "ironic",
    "истор.": "historical",
    # "канц.": "канцелярское",
    "книжн.": "literary",
    "ласк.": "diminutive",
    # "мол.": "молодёжное",
    "нар.-поэт.": "poetic",
    "нар.-разг.": "colloquial",
    # "научн.": "научное",
    "неодобр.": "disapproving",
    "неол.": "neologism",
    # "обсц.": "обсценное",
    "офиц.": "formal",
    # "патет.": "патетическое",
    "поэт.": "poetic",
    "презр.": "contemplative",
    "пренебр.": "derogatory",
    "прост.": "colloquial",
    # "проф.": "профессиональное",
    # "публиц.": "публицистическое",
    "разг.": "colloquial",
    "рег.": "regional",
    "ритор.": "rhetoric",
    "сленг.": "slang",
    "сниж.": "reduced",
    # "советск.": "советизм",
    "спец.": "special",
    "старин.": "archaic",
    "табу": "taboo",
    # "торж.": "торжественное",
    "трад.-нар.": "traditional",
    "трад.-поэт.": ["traditional", "poetic"],
    # "увелич.": "увеличительное",
    "уменьш.": "diminutive",
    "умласк.": ["diminutive", "endearing"],
    "унич.": "pejorative",
    "усилит.": "emphatic",
    "устар.": "obsolete",
    "фам.": "familiar",
    # "школьн.": "школьное",
    "шутл.": "humorous",
    "эвф.": "euphemistic",
    # "экзот.": "экзотизм",
    "экспр.": "expressively",
    # "эррат.": "эрративное",
}

# Предметные области
TOPICS = {
    "авиац.": "aeronautics",
    "автомоб.": "automotive",
    # "агрон.": "агрономическое",
    "алхим.": "pseudoscience",
    "альп.": "sports",
    "анат.": "medicine",
    "антроп.": "anthropology",
    "артилл.": "weaponry",
    "археол.": "history",
    "архит.": "architecture",
    "астрол.": "astrology",
    "астрон.": "astronomy",
    "библейск.": "religion",
    "биол.": "biology",
    "биохим.": "biochemistry",
    "ботан.": "botany",
    "бухг.": "finance",
    "вет.": "zoology pathology",
    "воен.": "military",
    "гастрон.": "medicine",
    "генет.": ["biology", "medicine"],
    "геогр.": "geography",
    "геод.": "geography",
    "геол.": "geology",
    "геометр.": "geometry",
    "геофиз.": "geology",
    "геральд.": "heraldry",
    "гидрол.": "geography",
    "гидротехн.": "engineering",
    "гляциол.": "geography",
    "горн.": "mining",
    "дипл.": "politics",
    "ж.-д.": "railways",
    "живоп.": "arts",
    # "животн.": "животноводство",
    "зоол.": "zoology",
    "игр.": "games",
    "информ.": "computing",
    "искусств.": "art-history",
    "ислам.": "Islam",
    "ихтиол.": "ichthyology",
    # "йогич.": "йогическое",
    "карт.": "card-games",
    "керам.": ["chemistry", "engineering"],
    "кино": "film",
    "кинол.": "dogs",
    "комп.": "computing",
    "косм.": "astronomy",
    "кулин.": "cuisine",
    # "культурол.": "культурологическое",
    "лес.": "business",
    "лингв.": "linguistics",
    "матем.": "mathematics",
    "машин.": "engineering",
    "мед.": "medicine",
    "металл.": "metallurgy",
    "метеорол.": "meteorology",
    "мех.": "mechanical-engineering",
    "микробиол.": "microbiology",
    "минер.": "mineralogy",
    "мифол,": "mythology",
    "морск.": "nautical",
    "муз.": "music",
    # "нефтегаз.": "нефтегазовая промышленность и нефтепереработка",
    "нумизм.": "numismatics",
    "океан.": "oceanography",
    "оккульт.": "mysticism",
    "опт.": ["physics", "engineering"],
    "орнитол.": "ornithology",
    "охотн.": "hunting",
    "палеонт.": "paleontology",
    "паразит.": "medicine",
    "парикмах.": "hairdressing",
    "плотн.": "carpentry",
    "полигр.": "printing",
    "полит.": "politics",
    "портн.": "textiles",
    "прогр.": "programming",
    "психиатр.": "psychiatry",
    "психол.": "psychology",
    "пчел.": "agriculture",
    "радио.": ["radio", "engineering"],
    "радиоэл.": ["radio", "electricity"],
    "рекл.": "marketing",
    "религ.": "religion",
    "рыбол.": "fishing",
    "с.-х.": "agriculture",
    "сексол.": "sexuality",
    # "скорн.": "скорняжное дело",
    "социол.": "sociology",
    # "спелеол.": "спелеологический",
    "спорт.": "sports",
    "стат.": "statistics",
    "столярн.": "carpentry",
    "строит.": "construction",
    "театр.": "theater",
    "текст.": "textiles",
    "телеком.": "telecommunications",
    "техн.": "engineering",
    "торг.": "commerce",
    "управл.": "management",
    "фант.": "fantasy",
    "фарм.": "pharmacology",
    "физ.": "physics",
    "физиол.": "physiology",
    "филат.": "philately",
    "филол.": "philology",
    "филос.": "philosophy",
    "фин.": "finance",
    "фолькл.": "folklore",
    "фотогр.": "photography",
    "хим.": "chemistry",
    "хоз.": "economics",
    # "хореогр.": "хореографическое",
    "церк.": "religion",
    "цирк.": "circus",
    "цитол.": "cytology",
    "шахм.": "chess",
    "швейн.": "sewing",
    "экол.": "ecology",
    "экон.": "economics",
    "эл.-техн.": "electrical-engineering",
    "эл.-энерг.": "electricity",
    "энтомол.": "entomology",
    "этногр": "ethnography",
    "этнолог.": "ethnology",
    "ювел.": "jewelry",
    "юр.": "legal",
}

# Жаргон
SLANG_TOPICS = {
    "автомоб. жарг.": "motorcycling",
    "арест.": "prison",
    "воен. жарг.": "military",
    "жарг. аним.": "anime",
    # "жарг. викип.": "жаргон википроектов"
    "интернет.": "Internet",
    "комп. жарг.": "computer",
    # "студ. жарг.": "студенческий жаргон",
    "техн. жарг.": "technical",
    "крим. и крим. жарг.": "criminology",
    "полит. жарг.": "politics",
    "жарг. нарк.": "drugs",
    "жарг. ЛГБТ": "LGBT",
    # "жарг. гом.": "жаргон гомосексуалов",
}

# Грамматические категории
GRAMMATICAL_TAGS = {
    "3л.": "impersonal",
    "адъектив.": "adjective",
    "безл.": "impersonal",
    "вводн. сл.": "parenthetic",
    "вин. п.": "accusative",
    "вопр.": "interrogative",
    # "восклиц.": "в восклицательных предложениях",
    "гл.": "verb",
    "дат. п.": "dative",
    "ед. ч.": "singular",  # Шаблон:ед
    "ж. р.": "feminine",
    "женск.": "feminine",
    "им. п.": "nominative",
    # "исх. п.": "исходный падеж",
    "исч.": "countable",
    "м. р.": "masculine",
    "местн. п.": "locative",
    "метоним.": "metonymically",
    "мн. ч.": "plural",  # Шаблон:мн, Шаблон:мн.
    "неисч.": "uncountable",
    "неодуш.": "inanimate",
    "неперех.": "intransitive",
    "нескл.": "indeclinable",
    # "обобщ": "",
    # "общ.": "",
    "одуш.": "animate",
    # "отриц.": "",
    "перех.": "transitive",
    # "повел.": "",
    "предик.": "predicative",
    # "предл. п.": "",
    # "прил.": "",
    # "прош.": "",
    # "разд. п.": "",
    # "род. п.": "",
    "собир.": "collective",
    # "ср. р.": "",
    "статив.": "stative",
    "субстантивир.": "substantive",
    # "сущ.": "",
    # "тв. п.": "",
    # https://ru.wiktionary.org/wiki/Категория:Шаблоны:Условные_сокращения
    "м.": "masculine",  # Шаблон:m
    "ср.": "neuter",  # Шаблон:n
    "ж.": "feminine",  # Шаблон:f
    "ж. мн.": ["feminine", "plural"],  # Шаблон:f.pl
    "несов.": "imperfective",  # Шаблон:impf
    "м./ж.": ["masculine", "feminine"],  # Шаблон:m/f
    "ср./м.": ["neuter", "masculine"],  # Шаблон:n/m
    "сов.": "perfective",  # Шаблон:pf
}

# Прочие сокращения
OTHER_TAGS = {
    "букв.": "literary",
    # "искаж.": "искажённое",
    "неправ.": "irregular",
    "перен.": "figuratively",
    "редк.": "rare",
    # "тж.": "",  # Шаблон:тж.
    "общая": "indefinite",
    "опред.": "definite",
    "счётн.": "count-form",
}

CASE_TAGS = {
    # Шаблон:сущ ru m a 1a
    "им.": "nominative",
    "р.": "genitive",
    "д.": "dative",
    "в.": "accusative",
    "тв.": "instrumental",
    "пр.": "prepositional",
    # Шаблон:сущ bg 7
    "зват.": "vocative",
}

TENSE_TAGS = {
    # Шаблон:Гл-блок
    "наст.": "present",
    "будущ.": "future",
    "прош.": "past",
    "будущее": "future",
}

MOOD_TAGS = {
    # Шаблон:Гл-блок
    "повелит.": "imperative",
}

PERSON_TAGS = {
    # Шаблон:Гл-блок
    "я": ["first-person", "singular"],
    "ты": ["second-person", "singular"],
    "он\nона\nоно": ["third-person", "singular"],
    "мы": ["first-person", "plural"],
    "вы": ["second-person", "plural"],
    "они": ["third-person", "plural"],
}

VOICE_TAGS = {
    # Шаблон:Гл-блок
    "пр. действ.": "active",
    "деепр.": "adverbial",
    "пр. страд.": "passive",
}


ALL_TAGS = {
    **STYLE_TAGS,
    **GRAMMATICAL_TAGS,
    **OTHER_TAGS,
    **CASE_TAGS,
    **TENSE_TAGS,
    **MOOD_TAGS,
    **PERSON_TAGS,
    **VOICE_TAGS,
}


def translate_raw_tags(data: WordEntry) -> None:
    raw_tags = []
    for raw_tag in data.raw_tags:
        raw_tag_lower = raw_tag.lower()
        if raw_tag_lower in ALL_TAGS:
            tr_data = ALL_TAGS[raw_tag_lower]
            if isinstance(tr_data, str):
                data.tags.append(tr_data)
            elif isinstance(tr_data, list):
                data.tags.extend(tr_data)
        elif hasattr(data, "topics"):
            tr_data = ""
            if raw_tag_lower in TOPICS:
                tr_data = TOPICS[raw_tag_lower]
            elif raw_tag_lower in SLANG_TOPICS:
                tr_data = SLANG_TOPICS[raw_tag_lower]
                if "slang" not in data.tags:
                    data.tags.append("slang")
            if isinstance(tr_data, str) and len(tr_data) > 0:
                data.topics.append(tr_data)
            elif isinstance(tr_data, list):
                data.topics.extend(tr_data)
        else:
            raw_tags.append(raw_tag)
    data.raw_tags = raw_tags

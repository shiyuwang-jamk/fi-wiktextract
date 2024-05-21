from .models import WordEntry

# Sense tags
# https://de.wiktionary.org/wiki/Vorlage:K
# https://de.wiktionary.org/wiki/Vorlage:K/Abk
K_TEMPLATE_TAGS = {
    "Abl.": "ablative",
    "Ablativ": "ablative",
    "abw.": "derogatory",
    "AE": "US",
    "AmE": "US",
    "adv.": "adverbial",
    "Akkusativ": "accusative",
    "alemann.": "Alemannic",
    "alemannisch": "Alemannic",
    "allg.": "general",
    "allgemein": "general",
    "alltagsspr.": "colloquial",
    "amtsspr.": "officialese",
    # "ansonsten": "otherwise",  # combined with other text
    "attr.": "attributive",
    # "auch": "also",
    "bair.": "Bavarian",
    "bairisch": "Bavarian",
    "bar.": "Bavarian",
    "BE": "British",
    "BrE": "British",
    "Bedva.": "outdated",
    "Bedvatd.": "outdated",
    # "bei": "",
    # "bes.": "especially",
    # "besonders": "especially",
    # "beziehungsweise": "",
    # "bzw.": "",
    # "bildungsspr.": "",
    # "bis": "",
    # "bisweilen": "",
    # "das": "",
    "Dativ": "dative",
    # "DDR": "",
    # "der": "",
    "dichter.": "poetic",
    # "die": "",
    "Dim.": "diminutive",
    "Dimin.": "diminutive",
    "Diminutiv": "diminutive",
    # "eher": "",
    "erzg.": "Erzgebirgisch",
    "erzgeb.": "Erzgebirgisch",
    "erzgebirgisch": "Erzgebirgisch",
    "euph.": "euphemistic",
    "fachspr.": "jargon",
    "fam.": "familiär",
    "fig": "figurative",
    "fig.": "figurative",
    # "früher": "",
    # "gegenwartslateinisch": "",
    "geh.": "gehoben",
    "Genitiv": "genitive",
    "gsm": "Swiss German",
    "häufig": "often",
    "haben": "auxiliary",
    "hebben": "auxiliary",
    "hauptsächlich": "primarily",
    "hist.": "historical",
    "ieS": "narrowly",
    "i.e.S.": "narrowly",
    "i. e. S.": "narrowly",
    # "im": "",
    # "in": "",
    # "in Bezug auf": "relational",
    "indekl.": "indeclinable",
    # "insbes.": "",
    "Instrumental": "instrumental",
    "intrans.": "intransitive",
    "intransitiv": "intransitive",
    # "iPl": "in plural",
    "iron.": "ironic",
    # "iwS": "",
    # "jugendspr.": "",
    "kinderspr.": "childish",
    "kirchenlateinisch": "Church Latin",
    "klasslat.": "Classical Latin",
    "klassischlateinisch": "Classical Latin",
    "kPl.": "no-plural",
    "kSg.": "no-singulative",
    "kSt.": "no-comparative",
    "landsch.": "regional",
    "lautm.": "onomatopoeic",
    "Ling.": "linguistics",
    "mA": "accusative",
    "md.": "Central German",
    "mdal.": "dialectal",
    "Med.": "medicine",  # topic
    # "meist": "mostly",
    # "meistens": "mostly",
    "metaphor.": "metaphoric",
    "meton.": "metonymically",
    "mG": "genitive",
    "mitteld.": "Central German",
    # "mitunter": "",
    "mlat.": "Medieval Latin",
    "mittellateinisch": "Medieval Latin",
    "mundartl.": "dialectal",
    "nDu.": "only-dual",
    "nigr.": "Niger",
    "nigrisch": "Niger",
    "nkLat.": "post-Classical Latin",
    "nachklassischlateinisch": "post-Classical Latin",
    "nlat.": "New Latin",
    "neulateinisch": "New Latin",
    "nordd.": "North German",
    "norddeutsch": "North German",
    "nordwestd.": "Northwestern Germany",
    "nPl.": "plural-only",
    "Österreich": "Austrian German",
    "österr.": "Austrian German",
    "österreichisch": "Austrian German",
    "ostfränkisch": "East Franconian German",
    "pej.": "pejorative",
    "poet.": "poetic",
    "PräpmG": "genitive prepositional",
    "PmG": "genitive prepositional",
    "reg.": "regional",
    "refl.": "reflexive",
    "reflexiv": "reflexive",
    # "respektive": "",
    "sal.": "casual",
    "scherzh.": "jocular",
    "schriftspr.": "literary",
    # "schülerspr.": "",
    "schwäb.": "Swabian",
    "schwäbisch": "Swabian",
    "Schweiz": "Swiss Standard German",
    "schweiz.": "Swiss Standard German",
    "schweizerisch": "Swiss Standard German",
    "Schweizerdeutsch": "Swiss German",
    "schweizerdeutsch": "Swiss German",
    # "seemannsspr.": "",
    "sein": "auxiliary verb",
    # "sehr": "",  # very
    # "seltener": "",  # rare
    # "seltener auch": "",
    "soldatenspr.": ["military", "slang"],
    # "sonderspr.": "",
    # "sonst": "",
    # "sowie": "",
    "spätlat.": "Late Latin",
    "spätlateinisch": "Late Latin",
    # "später": "",
    "speziell": "special",
    "südd.": "South German",
    "süddt.": "South German",
    # "techn.": "",
    # "teils": "",
    # "teilweise": "",
    "tlwva.": "outdated",
    "tlwvatd.": "outdated",
    "trans.": "transitive",
    "transitiv": "transitive",
    # "über": "",
    # "überwiegend": "mostly",
    "übertr.": "figurative",
    "ugs.": "colloquial",
    # "und": "",
    "ungebr.": "uncommon",
    "unpers.": "impersonal",
    "unpersönlich": "impersonal",
    # "ursprünglich": "",
    "va.": "outdated",
    "vatd.": "outdated",
    # "verh.": "",
    "volkst.": "popular",
    # "von": "",
    # "vor allem": "",
    # "vor allem in": "",
    "vul.": "vulgar",
    "vulg.": "vulgar",
    "vlat.": ["vulgar", "Latin"],
    "vulgärlat": ["vulgar", "Latin"],
    "vulgärlateinisch": ["vulgar", "Latin"],
    "wien.": "Vienna",
    "wienerisch": "Vienna",
    # "Wpräp": "",
    # "z. B.": "",
    # "z. T.": "",
    # "zijn": "",
    # "zum Beispiel": "",
    # "zum Teil": "",
    # "zumeist": "",
}

GENDER_TAGS = {
    "n": "neuter",
    "m": "masculine",
    "f": "feminine",
    # Vorlage:Deklinationsseite Adjektiv
    "Maskulinum": "masculine",
    "Femininum": "feminine",
    "Neutrum": "neuter",
}

NUMBER_TAGS = {
    # Vorlage:Deutsch Substantiv Übersicht
    "Singular": "singular",
    "Plural": "plural",
}

CASE_TAGS = {
    # Vorlage:Deutsch Substantiv Übersicht
    "Nominativ": "nominative",
    "Genitiv": "genitive",
    "Dativ": "dative",
    "Akkusativ": "accusative",
}

COMPARISON_TAGS = {
    # Vorlage:Deutsch Adjektiv Übersicht
    # Vorlage:Deklinationsseite Adjektiv
    "Positiv": "positive",
    "Komparativ": "comparative",
    "Superlativ": "superlative",
}

DECLENSION_TAGS = {
    # https://en.wikipedia.org/wiki/German_declension
    # Vorlage:Deklinationsseite Adjektiv
    "Starke Deklination": "strong",
    "Schwache Deklination": "weak",
    "Gemischte Deklination": "mixed",
}

OTHER_TAGS = {
    # Vorlage:Deklinationsseite Adjektiv
    "Prädikativ": "predicative",
}

GRAMMATICAL_TAGS = {
    **K_TEMPLATE_TAGS,
    **GENDER_TAGS,
    **NUMBER_TAGS,
    **CASE_TAGS,
    **COMPARISON_TAGS,
    **DECLENSION_TAGS,
    **OTHER_TAGS,
}


def translate_raw_tags(data: WordEntry) -> None:
    raw_tags = []
    for raw_tag in data.raw_tags:
        if raw_tag in GRAMMATICAL_TAGS:
            tag = GRAMMATICAL_TAGS[raw_tag]
            if isinstance(tag, str):
                data.tags.append(tag)
            elif isinstance(tag, list):
                data.tags.extend(tag)
        else:
            raw_tags.append(raw_tag)
    data.raw_tags = raw_tags

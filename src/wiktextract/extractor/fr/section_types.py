from wiktextract.config import POSSubtitleData

# the keys are the first argument of the `S` template
# https://fr.wiktionary.org/wiki/Modèle:S
# https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_des_sections
POS_SECTIONS: POSSubtitleData = {
    "adj": {"pos": "adj"},
    "adj-dém": {"pos": "adj", "tags": ["demonstrative"]},
    "adj-excl": {"pos": "adj", "tags": ["exclamatory"]},
    "adj-indéf": {"pos": "adj", "tags": ["indefinite"]},
    "adj-int": {"pos": "adj", "tags": ["interrogative"]},
    "adj-num": {"pos": "adj", "tags": ["numeral"]},
    "adj-pos": {"pos": "adj", "tags": ["possessive"]},
    "adj-rel": {"pos": "adj", "tags": ["relative"]},
    "adjectif": {"pos": "adj"},
    "adjectif dém": {"pos": "adj", "tags": ["demonstrative"]},
    "adjectif démonstratif": {"pos": "adj", "tags": ["demonstrative"]},
    "adjectif exc": {"pos": "adj", "tags": ["exclamatory"]},
    "adjectif exclamatif": {"pos": "adj", "tags": ["exclamatory"]},
    "adjectif ind": {"pos": "adj", "tags": ["indefinite"]},
    "adjectif indéfini": {"pos": "adj", "tags": ["indefinite"]},
    "adjectif int": {"pos": "adj", "tags": ["interrogative"]},
    "adjectif interrogatif": {"pos": "adj", "tags": ["interrogative"]},
    "adjectif num": {"pos": "adj", "tags": ["numeral"]},
    "adjectif numéral": {"pos": "adj", "tags": ["numeral"]},
    "adjectif pos": {"pos": "adj", "tags": ["possessive"]},
    "adjectif possessif": {"pos": "adj", "tags": ["possessive"]},
    "adjectif qualificatif": {"pos": "adj"},
    "adjectif rel": {"pos": "adj", "tags": ["relative"]},
    "adjectif relatif": {"pos": "adj", "tags": ["relative"]},
    "adv": {"pos": "adv"},
    "adv-ind": {"pos": "adv", "tags": ["indefinite"]},
    "adv-int": {"pos": "adv", "tags": ["interrogative"]},
    "adv-pron": {"pos": "adv"},
    "adv-rel": {"pos": "adv", "tags": ["relative"]},
    "adverbe": {"pos": "adv"},
    "adverbe ind": {"pos": "adv", "tags": ["indefinite"]},
    "adverbe indéfini": {"pos": "adv", "tags": ["indefinite"]},
    "adverbe int": {"pos": "adv", "tags": ["interrogative"]},
    "adverbe interrogatif": {"pos": "adv", "tags": ["interrogative"]},
    "adverbe pro": {"pos": "adv"},
    "adverbe pronominal": {"pos": "adv"},
    "adverbe rel": {"pos": "adv", "tags": ["relative"]},
    "adverbe relatif": {"pos": "adv", "tags": ["relative"]},
    "aff": {"pos": "affix"},
    "affixe": {"pos": "affix"},
    "art": {"pos": "article"},
    "art-déf": {"pos": "article", "tags": ["definite"]},
    "art-indéf": {"pos": "article", "tags": ["indefinite"]},
    "art-part": {"pos": "article", "tags": ["partial"]},
    "article": {"pos": "article"},
    "article déf": {"pos": "article", "tags": ["definite"]},
    "article défini": {"pos": "article", "tags": ["definite"]},
    "article ind": {"pos": "article", "tags": ["indefinite"]},
    "article indéfini": {"pos": "article", "tags": ["indefinite"]},
    "article par": {"pos": "article", "tags": ["partial"]},
    "article partitif": {"pos": "article", "tags": ["partial"]},
    "circon": {"pos": "circumfix", "tags": ["morpheme"]},
    "circonf": {"pos": "circumfix", "tags": ["morpheme"]},
    "circonfixe": {"pos": "circumfix", "tags": ["morpheme"]},
    "class": {"pos": "classifier"},
    "classif": {"pos": "classifier"},
    "classificateur": {"pos": "classifier"},
    "conj": {"pos": "conj"},
    "conj-coord": {"pos": "conj", "tags": ["coordinating"]},
    "conjonction": {"pos": "conj"},
    "conjonction coo": {"pos": "conj", "tags": ["coordinating"]},
    "conjonction de coordination": {"pos": "conj", "tags": ["coordinating"]},
    "copule": {"pos": "conj"},
    "dét": {"pos": "det"},
    "déterminant": {"pos": "det"},
    "encl": {"pos": "suffix", "tags": ["clitic"]},
    "enclitique": {"pos": "suffix", "tags": ["clitic"]},
    "gismu": {"pos": "verb", "tags": ["gismu"]},
    "idéophone": {"pos": "noun", "tags": ["ideophone"]},
    "inf": {"pos": "infix", "tags": ["morpheme"]},
    "infixe": {"pos": "infix", "tags": ["morpheme"]},
    "interf": {"pos": "interfix", "tags": ["morpheme"]},
    "interfixe": {"pos": "interfix", "tags": ["morpheme"]},
    "interj": {"pos": "intj"},
    "interjection": {"pos": "intj"},
    "lettre": {"pos": "character", "tags": ["letter"]},
    "loc": {"pos": "phrase"},
    "loc-phr": {"pos": "phrase"},
    "locution": {"pos": "phrase"},
    "locution phrase": {"pos": "phrase"},
    "locution-phrase": {"pos": "phrase"},
    "nom": {"pos": "noun"},
    "nom commun": {"pos": "noun"},
    "nom de famille": {"pos": "name", "tags": ["surename"]},
    "nom propre": {"pos": "name"},
    "nom scientifique": {"pos": "name", "tags": ["scientific"]},
    "nom-fam": {"pos": "name", "tags": ["surename"]},
    "nom-pr": {"pos": "name"},
    "num": {"pos": "num"},
    "numér": {"pos": "num"},
    "numéral": {"pos": "num"},
    "onom": {"pos": "onomatopoeia", "tags": ["onomatopoeic"]},
    "onoma": {"pos": "onomatopoeia", "tags": ["onomatopoeic"]},
    "onomatopée": {"pos": "onomatopoeia", "tags": ["onomatopoeic"]},
    "part": {"pos": "particle"},
    "part-num": {"pos": "particle", "tags": ["numeral"]},
    "particule": {"pos": "particle"},
    "particule num": {"pos": "particle", "tags": ["numeral"]},
    "particule numérale": {"pos": "particle", "tags": ["numeral"]},
    "patronyme": {"pos": "name", "tags": ["surename"]},
    "phrase": {"pos": "phrase"},
    "post": {"pos": "postp"},
    "postpos": {"pos": "postp"},
    "postposition": {"pos": "postp"},
    "procl": {"pos": "prefix", "tags": ["clitic"]},
    "proclitique": {"pos": "prefix", "tags": ["clitic"]},
    "pronom": {"pos": "pron"},
    "pronom dém": {"pos": "pron", "tags": ["demonstrative"]},
    "pronom démonstratif": {"pos": "pron", "tags": ["demonstrative"]},
    "pronom ind": {"pos": "pron", "tags": ["indefinite"]},
    "pronom indéfini": {"pos": "pron", "tags": ["indefinite"]},
    "pronom int": {"pos": "pron", "tags": ["interrogative"]},
    "pronom interrogatif": {"pos": "pron", "tags": ["interrogative"]},
    "pronom personnel": {"pos": "pron", "tags": ["person"]},
    "pronom pos": {"pos": "pron", "tags": ["possessive"]},
    "pronom possessif": {"pos": "pron", "tags": ["possessive"]},
    "pronom rel": {"pos": "pron", "tags": ["relative"]},
    "pronom relatif": {"pos": "pron", "tags": ["relative"]},
    "pronom réf": {"pos": "pron", "tags": ["person"]},
    "pronom réfléchi": {"pos": "pron", "tags": ["person"]},
    "pronom-adj": {"pos": "pron", "tags": ["adjective"]},
    "pronom-adjectif": {"pos": "pron", "tags": ["adjective"]},
    "pronom-dém": {"pos": "pron", "tags": ["demonstrative"]},
    "pronom-indéf": {"pos": "pron", "tags": ["indefinite"]},
    "pronom-int": {"pos": "pron", "tags": ["interrogative"]},
    "pronom-per": {"pos": "pron", "tags": ["person"]},
    "pronom-pers": {"pos": "pron", "tags": ["person"]},
    "pronom-pos": {"pos": "pron", "tags": ["possessive"]},
    "pronom-rel": {"pos": "pron", "tags": ["relative"]},
    "pronom-réfl": {"pos": "pron", "tags": ["person"]},
    "prov": {"pos": "proverb"},
    "proverbe": {"pos": "proverb"},
    "pré-nom": {"pos": "name", "tags": ["first name"]},
    "pré-verbe": {"pos": "preverb"},
    "préf": {"pos": "prefix", "tags": ["morpheme"]},
    "préfixe": {"pos": "prefix", "tags": ["morpheme"]},
    "prénom": {"pos": "name", "tags": ["first name"]},
    "prép": {"pos": "prep"},
    "préposition": {"pos": "prep"},
    "quantif": {"pos": "quantifier"},
    "quantificateur": {"pos": "quantifier"},
    "racine": {"pos": "root", "tags": ["morpheme"]},
    "rad": {"pos": "root", "tags": ["radical"]},
    "radical": {"pos": "root", "tags": ["radical"]},
    "rafsi": {"pos": "affix", "tags": ["rafsi"]},
    "substantif": {"pos": "noun"},
    "suf": {"pos": "suffix", "tags": ["morpheme"]},
    "suff": {"pos": "suffix", "tags": ["morpheme"]},
    "suffixe": {"pos": "suffix", "tags": ["morpheme"]},
    "symb": {"pos": "symbol"},
    "symbole": {"pos": "symbol"},
    "var-typo": {"pos": "typographic variant", "tags": ["alt-of"]},
    "variante par contrainte typographique": {
        "pos": "typographic variant",
        "tags": ["alt-of"],
    },
    "variante typo": {"pos": "typographic variant", "tags": ["alt-of"]},
    "variante typographique": {
        "pos": "typographic variant",
        "tags": ["alt-of"],
    },
    "verb pr": {"pos": "verb", "tags": ["pronominal"]},
    "verb-pr": {"pos": "verb", "tags": ["pronominal"]},
    "verbe": {"pos": "verb"},
    "verbe pronominal": {"pos": "verb", "tags": ["pronominal"]},
}

# map section arguments to pydantic fields
LINKAGE_SECTIONS: dict[str, str] = {
    "abrév": "abbreviation",
    "abréviations": "abbreviation",
    "antonymes": "antonyms",
    "app": "related",
    "apparentés": "related",
    "apr": "related",
    "dérivés autres langues": "derived",
    "dérivés int": "derived",
    "dérivés": "derived",
    "dial": "related",
    "dialectes": "related",
    "drv-int": "derived",
    "drv": "derived",
    "étymologiques": "related",
    "holo": "holonyms",
    "holonymes": "holonyms",
    "hyper": "hypernyms",
    "hyperonymes": "hypernyms",
    "hypo": "hyponyms",
    "hyponymes": "hyponyms",
    "méro": "meronyms",
    "méronymes": "meronyms",
    "paro": "paronyms",
    "paronymes": "paronyms",
    "phrases": "proverbs",
    "q-syn": "synonyms",
    "quasi-syn": "synonyms",
    "quasi-synonymes": "synonyms",
    "syn": "synonyms",
    "synonymes": "synonyms",
    "tropo": "troponyms",
    "troponymes": "troponyms",
    "var-dial": "related",
    "var-ortho": "related",
    "var": "related",
    "variantes dial": "related",
    "variantes dialectales": "related",
    "variantes dialectes": "related",
    "variantes ortho": "related",
    "variantes orthographiques": "related",
    "variantes": "related",
    "voc": "related",
    "vocabulaire apparenté": "related",
    "vocabulaire proche": "related",
    "vocabulaire": "related",
}

IGNORED_SECTIONS: frozenset[str] = frozenset(
    [
        "anagrammes",
        "anagramme",
        "anagr",
        "références",
        "référence",
        "réf",
        "ref",
        "sources",
        "src",
        "bibliographie",
        "bib",
        "citations",
        "cit",
    ]
)

COMPOUNDS_SECTIONS: frozenset[str] = frozenset(["composés", "compos"])

ETYMOLOGY_SECTIONS: frozenset[str] = frozenset(["étymologie", "étym", "etym"])

INFLECTION_SECTIONS: frozenset[str] = frozenset(
    ["déclinaison", "décl", "conjugaison", "conjug"]
)

NOTES_SECTIONS: frozenset[str] = frozenset(["notes", "note"])

PRONUNCIATION_SECTIONS: frozenset[str] = frozenset(
    ["prononciation", "pron", "prononciations"]
)

TRANSLATION_SECTIONS: frozenset[str] = frozenset(
    ["traductions", "trad", "traductions à trier", "trad-trier", "trad trier"]
)

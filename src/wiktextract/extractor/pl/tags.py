from .models import WordEntry

# Help:Abbreviations used in Wiktionary
# https://pl.wiktionary.org/wiki/Pomoc:Skróty_używane_w_Wikisłowniku
# Category:Shortcut templates
# https://pl.wiktionary.org/wiki/Kategoria:Szablony_skrótów
TAGS = {
    "abl.": "ablative",
    # "akust.": "",
    "aor.": "aorist",
    "arab.": "Arabic",
    "bałt.": "Baltic",
    "bask.": "Basque",
    "bezok.": "infinitive",
    "bezosob.": "impersonal",
    "bibl.": "Biblical",
    "blm": "no-plural",
    "blp": "no-singulative",
    "Bm": "Bokmål",
    "bośn.": "Bosnian",
    "brytań.": "British",
    "bułg.": "Bulgarian",
    "bwr.": "Bavarian",
    "celt.": "Celtic",
    "chiń.": "Chinese",
    "chorw.": "Croatian",
    "cs.": "Church-Slavonic",
    "czes.": "Czech",
    "depr.": "depreciative",
    "dial.": "dialectal",
    "dk": "perfective",
    "dosł.": "literally",
    "du": "dual",
    "dysfem.": "dysphemism",
    "dysk.": "discourse",
    "dźwięk.": "onomatopoeic",
    "egip.": "Egyptian",
    "ekspr.": "expressively",
    "el.": "Greek",
    "erud.": "eruditely",
    "eufem.": "euphemistic",
    "ew.": "alternative",
    "ezot.": "esoteric",
    "franc.": "French",
    "galic.": "Galician",
    "germ.": "Germanic",
    "gr.": "Ancient-Greek",
    "grec.": "Ancient-Greek",
    "grub.": "offensive",
    "grzecz.": "polite",
    "gw.": "dialectal",
    "hebr.": "Hebrew",
    "hin.": "Hindi",
    "hiszp.": "Spanish",
    "honor.": "honorific",
    "ims.": "participle",
    "ind.": "India",
    "infant.": "childish",
    "irl.": "Irish",
    "iron.": "ironic",
    "iterat.": "iterative",
    "jap.": "Japanese",
    "kanad.": "Canadian-English",
    "kanad. franc.": "Canadian-French",
    "kant.": "Cantonese",
    "katal.": "Catalan",
    "kathar.": "Katharevousa",
    "kaz.": "Kazakh",
    "kor.": "Korean",
    "kor. płd.": "South-Korean",
    "kor. płn.": "North-Korean",
    "korn.": "Cornish",
    "książk.": "literary",
    "lekcew.": "pejorative",
    "lewant. arab.": "Levantine-Arabic",
    "libij. arab.": "Libyan-Arabic",
    "licz.": "numeral",
    "licz. gł.": "cardinal",
    "licz. porz.": "ordinal",
    "litew.": "Lithuanian",
    "lm": "plural",
    "lm m": ["plural", "masculine"],
    "lm nm": ["plural", "nonvirile"],
    "lp": "singular",
    "lud.": "vernacular",
    "lwow.": ["Lviv", "dialectal"],
    "łac.": "Latin",
    "łac.kośc.": ["Ecclesiastical", "Latin"],
    "łot.": "Latvian",
    "m": "masculine",
    "mac.": "Macedonian",
    "malaj.": "Malay",
    "marok.": "Moroccan",
    "międzyr.": "interfix",
    "młodz.": "youth",
    "mong.": "Mongolian",
    "mong. klas.": "Classical-Mongolian",
    "moz.": "Mozambique",
    "m.-os.": ["masculine", "personal"],
    "mrz": ["masculine", "inanimate"],
    "mzw": ["masculine", "animate"],
    "n": "neuter",
    "nah": "Nahuatl",
    "nbk.": "Bokmål",
    "ndk": "imperfective",
    "neol.": "neologism",
    "neutr.": "neutral",
    "n.gr.": "Modern-Greek",
    "niderl.": "Dutch",
    "nieofic.": "unofficially",
    "niem.": "German",
    "niem. RFN": "Standard-German",
    "nieodm.": "uninflected",
    "nieos.": "impersonal",
    "niepopr.": "incorrectly",
    "n.łac.": "Neo-Latin",
    "nm.-os.": "nonvirile",
    "nn": "Nynorsk",
    "norw.": "Norwegian",
    "nowozel": "New-Zealand",
    "nprzech.": "intransitive",
    "nwh.": "Navajo",
    "nżw": "inanimate",
    "nord.": "Nordic",
    "obraź": "offensive",
    "odczas.": "verbal",
    "odm.": "inflected",
    "odprzym.": "deadjectival",
    "odrzecz.": "substantival",
    "ofic.": "officially",
    "ogsłow.": "Common-Slavic",
    "określ.": "determiner",
    "os.": "person",
    "oset.": "Ossetian",
    "osm.": "Ottoman",
    "oznajm.": "indicative",
    "partyk.": "particle",
    "paszto": "Pashto",
    "Prt.": "partitive",
    "pejor.": "pejorative",
    "pers.": "Persian",
    "peryfr.": "periphrastic",
    "p.gr": "Late-Greek",
    "pieszcz.": "endearing",
    "p.łac.": "Late-Latin",
    "płdbraz.": "Brazil",
    "płnlap.": "Northern-Sámi",
    "podn.": "elevatedly",
    "poet.": "poetic",
    "pogard.": "scornfully",
    "pol.": "Polish",
    "poł.": "Polabian",
    "port.": "Portuguese",
    "posp.": "commonly",
    "postp.": "postpositional",
    "pot.": "colloquial",
    "pozn.": ["Poznań", "regional"],
    "pragerm.": "Proto-Germanic",
    "praindoeur.": "Proto-Indo-European",
    "pranord.": "Proto-Norse",
    "prasł.": "Proto-Slavic",
    "praturk.": "Proto-Turkic",
    "prawdop.": "presumably",
    "prow.": "Provençal",
    "przech.": "transitive",
    "przecz.": "negation",
    "przedr.": "prefix",
    "przen.": "metaphoric",
    "przest.": "obsolete",
    "przesz.": "past",
    "przyim.": "prepositional",
    "przym.": "adjective",
    "przyp.": "subjunctive",
    "M.": "nominative",
    "Nom.": "nominative",
    "D.": "genitive",
    "Gen.": "genitive",
    "C.": "dative",
    "Dat.": "dative",
    "B.": "accusative",
    "Akk.": "accusative",
    "N.": "instrumental",
    "Ms.": "locative",
    "W.": "vocative",
    "adess.": "adessive",
    "all.": "allative",
    "ess.": "essive",
    "part.": "partitive",
    "przyr.": "suffix",
    "przysł.": "adverb",
    "przysz.": "future",
    "psych.": "psychology",
    "pszcz.": "beekeeping",
    "p. uwsp.": "modern",  # "(p. uwsp.)" from template "uwsp"
    "polinez.": "Polynesian",
    "qu.": "Quechua",
    "quen.": "Quenya",
    "rzym.": "Roman",
    "słow.": "Slavic",
    "sumer.": "Sumerian",
    # Category:Acronym templates - grammar
    # https://pl.wiktionary.org/wiki/Kategoria:Szablony_skrótów_-_gramatyka
    # gender types in POS line
    "męski": "masculine",
    "męskozwierzęcy": ["masculine", "animate"],
    "męskorzeczowy": ["masculine", "inanimate"],
    "niepoliczalny": "uncountable",
    "nieżywotny": "inanimate",
    "nijaki": "neuter",
    "policzalny": "countable",
    "przechodni": "transitive",
    "żeński": "feminine",
    "żywotny": "animate",
    "dzierżawczy": "possessive",
    "niedokonany": "imperfective",
    "relacyjny": "relational",
    # sound tags
    "bryt. (RP)": ["British", "Received-Pronunciation"],
    "amer.": "US",
    # "odmiana-rzeczownik-polski" template
    "liczba pojedyncza": "singular",
    "liczba mnoga": "plural",
    "mianownik": "nominative",
    "dopełniacz": "genitive",
    "celownik": "dative",
    "biernik": "accusative",
    "narzędnik": "instrumental",
    "miejscownik": "locative",
    "wołacz": "vocative",
    # "odmiana-przymiotnik-polski" template
    "mos/mzw": ["masculine", "animate"],
    "ż": "feminine",
    "mos": "masculine",
    "nmos": "nonvirile",
    "stopień wyższy": "comparative",
    "stopień najwyższy": "superlative",
}

TOPICS = {
    "adm.": "administration",
    "agrot.": "agrotechnology",
    "alch.": "alchemy",
    "anat.": "anatomy",
    "antrop.": "anthropology",
    "arachn.": "arachnology",
    "archit.": "architecture",
    "archeol.": "archeology",
    "astr.": "astronomy",
    "astrol.": "astrology",
    "astronaut.": "astronautics",
    "bank.": "banking",
    # "bibliot.": "",
    "biochem.": "biochemistry",
    "biol.": "biology",
    # "biur.": "",
    "bot.": "botany",
    "bud.": "construction",
    "ceram.": "ceramics",
    "chem.": "chemistry",
    "choreogr.": "choreography",
    "cukiernictwo.": "confectionery",
    "cybern.": "cybernetics",
    # "daw.": "",
    "demogr.": "demography",
    "dendr.": "dendrology",
    "drewn.": "woodworking",
    "druk.": "printing",
    "dypl.": "diplomacy",
    "eduk.": "education",
    "ekol.": "ecology",
    "ekon.": "economics",
    "elektr.": "electricity",
    "elektron.": "electronics",
    "enol.": "oenology",
    "ent.": "entomology",
    "etn.": "ethnography",
    "etym.": "etymology",
    "fant.": "speculative-fiction",
    "farm.": "pharmacology",
    "felinol.": "felinology",
    "filatel.": "philately",
    "film.": "film",
    "filoz.": "philosophy",
    "finans.": "finance",
    "fitopatol.": "phytopathology",
    "fiz.": "physics",
    "fizj.": "physiology",
    "flis.": "timber-rafting",
    "folk.": "folklore",
    "fonet.": "phonetics",
    "form. słow.": "word-forming",
    "fot.": "photography",
    "fryzj.": "hairdressing",
    "garb.": "tanning",
    "gastr.": "gastronomy",
    "genet.": "genetics",
    "geod.": "geodesy",
    "geofiz.": "geophysics",
    "geogr.": "geography",
    "geol.": "geology",
    "geom.": "geometry",
    "gend. st.": "gender-studies",
    "ginek.": "gynaecology",
    "górn.": "mining",
    "gram.": "grammar",
    "gry komp.": "computer games",
    "hand.": "trade",
    "harc.": "scouting",
    "herald.": "heraldry",
    "herp.": "herpetology",
    "hig.": "hygienic",
    "hipol.": "hippology",
    "hist.": "history",
    "hotel.": "hotel-industry",
    "hutn.": "metallurgy",
    "hydraul.": "hydraulics",
    "hydrol.": "hydrology",
    "icht.": "ichthyology",
    "ikonogr.": "iconography",
    "inform.": "computer-science",
    "jedn. miar.": "units-of-measure",
    "jedn. monet.": "units-of-monetary",
    "jeźdz.": "equestrianism",
    "jęz.": "linguistics",
    "jubil.": "jewelry",
    "kartogr.": "cartography",
    "kolej.": "railways",
    "konserwat.": "conservation",
    "kosmet.": "cosmetics",
    "kośc.": "ecclesiastical",
    "kraw.": "tailoring",
    "krym.": "criminology",
    "kryptogr.": "cryptography",
    "krystal.": "crystallography",
    "księg.": "accounting",
    "kulin.": "culinary",
    "kult.": "cultural-studies",
    "kynol.": "cynology",
    "leśn.": "forestry",
    "liter.": "literature",
    "log.": "logic",
    "lotn.": "aviation",
    "łow.": "hunting",
    "mar.": "nautical",
    "mat.": "mathematics",
    "mebl.": "furniture",
    "mech.": "mechanics",
    "med.": "medicine",
    "met.": "metallurgy",
    "meteorol.": "meteorology",
    "metrol.": "metrology",
    "mikol.": "mycology",
    "mikrobiol.": "microbiology",
    "miner.": "mineralogy",
    "mit.": "mythology",
    "młyn.": "milling",
    "monet.": "monetary-unit",
    "mors.": "maritime",
    "mot.": "automotive",
    "muz.": "musicology",
    "myśl.": "hunting",
    "nauk.": "sciences",
    "nawig.": "navigation",
    "numizm.": "numismatics",
    "obuw.": "footwear",
    "oceanogr.": "oceanography",
    "odl.": "foundry",
    "odzież.": "clothing-industry",
    "opt.": "optics",
    "ornit.": "ornithology",
    "paleoantrop.": "paleoanthropology",
    "paleont.": "paleontology",
    "papier.": "papermaking",
    "pedag.": "pedagogy",
    "poczt.": "mail",
    "poligr.": "printing",
    "polit.": "political-science",
    "praw.": "law",
    "przestęp.": "criminal",
}


def translate_raw_tags(data: WordEntry) -> None:
    raw_tags = []
    for raw_tag in data.raw_tags:
        if not check_tag(data, raw_tag):
            found_tag = False
            for part_of_tag in raw_tag.split():
                if check_tag(data, part_of_tag):
                    found_tag = True
            if not found_tag:
                raw_tags.append(raw_tag)
    data.raw_tags = raw_tags


def check_tag(data: WordEntry, raw_tag: str) -> bool:
    # return `True` if found tag or topic
    if raw_tag in TAGS and hasattr(data, "tags"):
        tag = TAGS[raw_tag]
        if isinstance(tag, str) and tag not in data.tags:
            data.tags.append(tag)
        elif isinstance(tag, list):
            for t in tag:
                if t not in data.tags:
                    data.tags.append(t)
    elif raw_tag in TOPICS and hasattr(data, "topics"):
        topic = TOPICS[raw_tag]
        if isinstance(topic, str):
            data.topics.append(topic)
        elif isinstance(topic, list):
            data.topics.extend(topic)
    else:
        return False
    return True

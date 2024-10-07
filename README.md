# Why this fork

The original repo pulls Finnish data from the domain `en.wiktionary.org`, which lacks some information from the Finnish counterpart `fi.wiktionary.org` (hereinafter referred to as fi.wikt).

This fork will be an attempt at pulling data from fi.wikt instead, focusing on collecting exceptions in Finnish verb conjugation from NSK and KOTUS, e.g. the Finnish word `sortaa` in [fi.wikt](https://fi.wiktionary.org/wiki/sortaa) versus in [en.wikt](https://en.wiktionary.org/wiki/sortaa).

# TODO
- [ ] Write `fi.lua` file in `languages/lua`
- [ ] Write `src/wiktextextract/data/fi/config.json` copied from `../en`
- [ ] Write extractor scripts in `src/wiktextextract/extractor/fi`
- [ ] Find enough time for all tasks.

# TOREAD; known so far
- All modules at fi.wikt: https://fi.wiktionary.org/wiki/Toiminnot:Kaikki_sivut?from=&to=&namespace=828 via https://fi.wiktionary.org/wiki/Toiminnot:Tilastot via https://meta.wikimedia.org/wiki/Wiktionary#List_of_Wiktionaries
    - at en.wikt: https://en.wiktionary.org/wiki/Category:Modules
        - Download from [kaikki.org](https://kaikki.org/dictionary/rawdata.html)
- All templates at fi.wikt: https://fi.wiktionary.org/wiki/Luokka:Mallineet
    - en.wikt template download also from kaikki.org
- All categories concerning Finnish at fi.wikt: https://fi.wiktionary.org/wiki/Toiminnot:Kaikki_sivut?from=Suom&to=&namespace=14
    - [Suomen kielen verbit](https://fi.wiktionary.org/wiki/Luokka:Suomen_kielen_verbit)
        - [... joilta puuttuu taivutustyyppi (670 S)](https://fi.wiktionary.org/wiki/Luokka:Suomen_verbit,_joilta_puuttuu_taivutustyyppi)
- https://kaiko.getalp.org/about-dbnary/ via [Ylonen , T 2022 , Wiktextract: Wiktionary as Machine-Readable Structured Data . in N Calzolari , F Béchet & P Blache, et al. (eds) , Proceedings of the 13th Conference on Language Resources and Evaluation (LREC) . European Language Resources Association (ELRA) , Paris , pp. 1317-1325 , International Conference on Language Resources and Evaluation , Marseille , France , 20/06/2022 .](https://helda.helsinki.fi/server/api/core/bitstreams/ff773457-674a-46e7-9d6e-0b14dca7e9e1/content)
- Using Lua scripts with [Scribunto](https://en.wiktionary.org/wiki/Wiktionary:Scribunto#:~:text=the%20source-code%20of%20a%20Scribunto%20module%20is)
- [Lua for beginners](https://en.wikipedia.org/wiki/Help:Lua_for_beginners)
- [MediaWiki API](https://fi.wiktionary.org/w/api.php)
    - parsing wikitext, [stackoverflow](https://stackoverflow.com/questions/52816628/how-do-i-parse-wikitext-using-built-in-mediawiki-support-for-lua-scripting)
## Searching across GitHub
- Parsing fi.wikt dump: [a bash script](https://github.com/flammie/omorfi/blob/fd558b22c4cf03e49f9939674641781ea70d9bac/src/externals/fiwikt2omorfi.bash#L10)
- Parse wikitext->xml [in Java](https://github.com/korhoj/wiktionary-convert-no-db/blob/6a82ef335ada6398c11a30c3cc7d85e42e283158/wikt2xmlfull/src/wiktionary/to/xml/full/ParseLangsFi.java#L23)

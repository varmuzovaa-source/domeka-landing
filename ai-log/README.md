# Domeka — záznam práce s AI

Tato složka dokládá práci s AI při přípravě výběrového úkolu Domeka.

## Doporučený začátek

[Postup práce a rozhodnutí](POSTUP-A-ROZHODNUTI.md) vysvětluje obchodní cíl, návrh stránky, volbu lead magnetu, práci s AI a rozsah ověření. Jde o dodatečně zpracovaný přehled; autentický průběh je doložen historickým přepisem níže.

## Průběh práce

První verze vznikla s ChatGPT. Následné přepracování stránky, textů a dokumentace probíhalo s Claude Code. Po této části následovala jazyková, marketingová a technická revize s Codexem. Závěrečné změny a výsledky kontrol jsou popsány v `../DESIGN_DECISIONS.md` a `../QA_RELEASE_CHECKLIST.md`.

## Obsah složky

- **`claude-code-export.txt`** — historický textový přepis relace Claude Code, vytvořený převodem exportovaných dat `transcript.jsonl`. Obsahuje původní pokyny, odpovědi a záznam použitých nástrojů; dlouhé výstupy byly zkráceny. Není doslovným výstupem příkazu `/export` a nezachycuje následnou revizi v Codexu.
- **`redakcne-upravena-zadani.md`** — dodatečná jazyková a strukturální revize vybraných pokynů autorky. Slouží jako čitelný doprovod. Nejde o původní prompty v jejich skutečně odeslaném znění a nenahrazuje historický přepis. Odkazy na řádky umožňují porovnat obě verze.

## Soukromí a úpravy přepisu

Z historického přepisu byly vypuštěny výsledky čtení soukromé pošty, e-mailové adresy a jména třetích osob byly anonymizovány. Dále byly vypuštěny skryté systémové instrukce a zkráceny dlouhé výstupy nástrojů. Tyto zásahy jsou přiznány v úvodu souboru.

Původní pokyny v historickém přepisu nebyly při následné redakční revizi nahrazeny uhlazenějšími formulacemi. Upravené znění je oddělené, aby bylo zřejmé, jak práce skutečně probíhala a co bylo přeformulováno dodatečně.

## Vztah k požadovanému exportu

Zadání výslovně požaduje export konverzace příkazem `/export`. Přiložený převedený přepis není vydáván za jeho doslovný výstup. Pokud zadavatel vyžaduje přesně tento formát, je potřeba doplnit přímý export ze zdrojové relace Claude Code. Redakčně upravená zadání tento požadavek nenahrazují.

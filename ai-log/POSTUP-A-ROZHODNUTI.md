# Domeka — postup práce a rozhodnutí

Tento přehled vznikl dodatečně pro orientaci v odevzdání. Shrnuje záměr, vývoj řešení a doložené kontroly. Není doslovnou konverzací s AI ani nezávislým měřením obchodních výsledků.

## 1. Obchodní cíl a cílová skupina

Cílem zadání jsou investice od 50 000 Kč, nikoli samotný počet formulářů. Každý kontakt spotřebovává rozpočet na reklamu a čas poradce. Návrh proto zohledňuje jak získání kontaktu, tak jeho předběžnou kvalifikaci.

Stránka je určená především českým návštěvníkům nad 50 let, kteří přicházejí z mobilu a nemusí mít s dluhopisy zkušenost. Text vysvětluje vztah mezi investorem a firmou, pevnou sazbu, termín vrácení jistiny i možnost ztráty. Zajištění není prezentováno jako záruka návratnosti.

## 2. Proč tato struktura stránky

Úvod pojmenovává produkt, sazbu, minimum, splatnost a četnost výplat. Následující části vysvětlují podnikání firmy, podmínky, zdroj peněz na úroky a rizika. Na mobilu jsou základní parametry a upozornění na riziko před kalkulačkou.

Kalkulačka převádí procenta na konkrétní částky a přenáší zvolenou investici do formuláře. Odlišuje součet úroků od vrácené jistiny. Příklad nájemného ukazuje potřebný rozsah příjmů, ale výslovně upozorňuje, že hrubé nájemné není zisk a samo nedokládá schopnost splácet.

Vizuální návrh využívá architektonickou fotografii, výraznou typografii, střídmé barvy a opakovanou hlavní akci. Ilustrační fotografie nejsou vydávány za skutečný majetek firmy. Pohyb slouží pouze jako krátká odezva ovládání a respektuje nastavení omezeného pohybu.

## 3. Lead magnet a okamžik žádosti o kontakt

„Pět otázek před nákupem firemního dluhopisu“ je skutečné dvoustránkové PDF. Obsahuje kontrolní otázky, informace o tom, kde hledat odpovědi, varovné signály, tabulku úroků pro čtyři částky a deset dotazů pro poradce. Hodnota materiálu je vysvětlena veřejným náhledem ještě před kontaktem.

Finální cesta je:

**Nabídka → vysvětlení a rizika → náhled průvodce → částka a termín → kontakt → hotové PDF.**

E-mail je výchozí kontaktní údaj. Člověk s částkou alespoň 50 000 Kč a termínem do tří měsíců může místo něj uvést telefon a požádat o konzultaci. Lidé pod minimem nebo s pozdějším či nejistým záměrem mají vzdělávací cestu bez nabídky obchodního hovoru.

Dřívější verze umožňovala dokončení bez kontaktu. Po revizi byla tato volba změněna, protože volné stažení materiálu samo neplnilo hlavní požadavek na získání kontaktu. Původní rozhodnutí je dohledatelné v historii; není vydáváno za finální řešení.

Jde o návrhovou hypotézu. Deklarovaná částka a termín nejsou důkazem vhodnosti investice. V ostrém provozu by se sledovala dosažitelnost kontaktů, poradcem přijaté kontakty, skutečné investice a cena za investora. K ověření jsou navrženy varianty úvodu, pořadí formuláře a názvu průvodce.

## 4. Jak byla využita AI

První verze vznikla s ChatGPT. Další přepracování probíhalo s Claude Code: struktura stránky, vizuální zpracování, texty, formulář, dokumentace a nasazení. Průběžné připomínky autorky směřovaly k odstranění nevhodné fotografie, spisovné češtině, srozumitelnosti a lepší návaznosti obchodní cesty.

V podkladech jsou uvedeny reference z Refero, ilustrační fotografie vytvořené AI a zvažování MotionSites. Nástroje sloužily k přípravě výstupu; jejich použití samo není důkazem jeho kvality.

Závěrečná revize s Codexem opravila jazykové a významové chyby, výpočet počtu bytů, překrývající se intervaly investic a nepravdivá potvrzení o odesílání. Doplnila kontaktní podmínku průvodce a upravila mobilní pořadí informací, fokus a odezvu ovládání.

Přehled návaznosti doložených změn:

| Etapa | Příklady v historii |
|---|---|
| První redesign a větvení formuláře | `49dcb2b` |
| Fotografie, vysvětlení výpočtu a průvodce | `1fb6c0e`, `76b40dd` |
| Jazykové a technické úpravy | `d3930a9`, `411841f` |
| Skutečné PDF, patička a kalkulačka | `0bc1b1e`, `a32c2ed`, `142612d` |
| Poslední úpravy původní realizace | `2ffbd43`, `0f3fe8f` |
| Závěrečná oprava textů a kontaktní cesty | `63123f6` |

Jedná se o postupné revize jediné větve `main`, nikoli o oddělené vývojové větve.

## 5. Co je ověřené a co zůstává otevřené

Ověřeno bylo všech 20 kombinací částky a termínu v běžném Chrome. Vyzkoušena je e-mailová i telefonní cesta, odmítnutí prázdných a chybných údajů a zobrazení PDF po dokončení. Dalších 41 kontrol proběhlo v simulovaném DOM; nejde o náhradu vizuálního testu.

Stránka byla vykreslena v 18 šířkách od 320 do 1440 px bez vodorovného přetékání. Obě strany přegenerovaného PDF byly vizuálně zkontrolovány. Přesný rozsah a omezení jsou v [kontrolním seznamu](../QA_RELEASE_CHECKLIST.md).

Nové měření Lighthouse a úplná kontrola přístupnosti nejsou doloženy. Historické skóre se nepřenáší na současnou verzi. Obchodní výkon nebyl měřen.

Podle zadání jde o ukázku bez ukládání či odesílání kontaktů. Potvrzení nepředstírá skutečné doručení nebo telefonát. PDF je v rozhraní až za kontaktním krokem; statický soubor však není serverově chráněný.

Před skutečnou kampaní jsou potřeba ověřené údaje emitenta a emise, právní a datové podklady, podklady k zajištění, vhodné fotografie a funkční zpracování kontaktů, doručování a měření.

## Podklady k tomuto přehledu

- [Historický přepis práce s Claude Code](claude-code-export.txt) — převod exportovaných dat, se zkrácenými výstupy a anonymizací; nikoli doslovný výstup `/export`.
- [Redakčně upravená zadání](redakcne-upravena-zadani.md) — dodatečné přeformulování vybraných pokynů, nikoli původně odeslané prompty.
- [Technické ověření](../QA_RELEASE_CHECKLIST.md).
- [Historie změn](https://github.com/varmuzovaa-source/domeka-landing/commits/main/).

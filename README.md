# Domeka — investiční landing page

Praktický úkol pro výběrové řízení na pozici Junior AI Developer. Firma, emise a doplněné obchodní údaje jsou fiktivní. Cílem je předvést srozumitelnou mobilní nabídku a získání předběžně kvalifikovaného kontaktu pro poradce.

**[Živá stránka](https://domeka-landing.vercel.app)** · **[Postup práce a rozhodnutí](ai-log/POSTUP-A-ROZHODNUTI.md)** · **[Záznam práce s AI](ai-log/README.md)** · **[Ověření a limity](QA_RELEASE_CHECKLIST.md)**

## Obchodní návrh

Stránka má podpořit investice od 50 000 Kč. Počet vyplněných formulářů je pouze průběžná metrika. Proto vysvětluje produkt a rizika, představuje hodnotu průvodce a před žádostí o kontakt zjišťuje částku a termín.

Lead magnet „Pět otázek před nákupem firemního dluhopisu“ je vyrobený jako dvoustránkové PDF. Obsahuje kontrolní otázky, varovné signály, tabulku úroků a deset dotazů pro poradce. Veřejný je náhled, hotový soubor je v uživatelské cestě až za kontaktem.

**Nabídka → podmínky a rizika → náhled průvodce → dvě otázky → kontakt → PDF.**

| Odpovědi | Další postup |
|---|---|
| Od 50 000 Kč a do tří měsíců | Průvodce za e-mail, nebo telefon místo e-mailu při zájmu o konzultaci. |
| Od 50 000 Kč, později nebo nejistý termín | Průvodce za e-mail, bez nabídky hovoru. |
| Pod 50 000 Kč | Vzdělávací cesta za e-mail, bez nabídky hovoru a tlaku na navýšení částky. |
| Částka zatím neurčená | Informační cesta za e-mail, bez nabídky hovoru. |

Kalkulačka ukazuje hrubé úroky a přenáší částku do formuláře. Samotné odpovědi nepotvrzují vhodnost investice ani dosažitelnost kontaktu.

## Co skutečně funguje

- Statický web v HTML, CSS a JavaScriptu bez knihoven.
- Kalkulačka, návaznost částky, větvení formuláře a validace kontaktu.
- Zpřístupnění PDF po vyplnění kontaktního kroku.
- Přehledné vysvětlení jistiny, výplat a rizik; jemná odezva ovládání s podporou omezeného pohybu.

**Formulář nic neukládá ani neodesílá.** Používají se testovací údaje a dokončení nepředstírá skutečný e-mail ani telefonát. Zadání funkční sběr kontaktů nevyžaduje. Soubor PDF není serverově chráněný; znalost přímé adresy umožní jeho otevření bez formuláře.

## Doplněné a modelové údaje

Ze zadání pocházejí název Domeka, podnikání v obnově a pronájmu bytových domů, cíl emise 150 mil. Kč, minimum 50 000 Kč, čtyřletá splatnost, pevný čtvrtletně vyplácený úrok a obecné zajištění domy firmy.

Pro návrh byly doplněny sazba 7,2 % ročně, upisování do 31. 3. 2027, působení od roku 2012, 46 opravených domů, přibližně 520 pronajatých bytů, obsazenost 97 %, podrobnosti zajištění, nájemné 14 000 Kč, kontaktní údaje a ilustrační fotografie vytvořené AI. Vlastním návrhem je také průvodce a kvalifikační cesta. Nejsou uvedeny vymyšlené reference ani schválení regulátora.

Výpočet pro 50 000 Kč: 900 Kč čtvrtletně, 3 600 Kč ročně a 14 400 Kč za čtyři roky, před zdaněním a při plnění závazků firmy. Úroky z celé emise činí 10,8 mil. Kč ročně, průměrně 900 000 Kč měsíčně. To odpovídá hrubému nájemnému nejméně 65 celých plně pronajatých bytů po 14 000 Kč; provozní náklady a splacení jistiny vyžadují další prostředky.

## Ověření a omezení

V běžném Chrome bylo vyzkoušeno všech 20 kombinací odpovědí i e-mailová a telefonní cesta. Dalších 41 kontrol logiky proběhlo v simulovaném DOM. V 18 vykreslených šířkách od 320 do 1440 px nebylo zjištěno vodorovné přetékání. Obě strany PDF byly vizuálně zkontrolovány.

Nové Lighthouse, úplný audit WCAG, VoiceOver, kompletní ruční průchod klávesnicí a ostatní prohlížeče nejsou doloženy. Starší měření 99/100/100/100 se nevztahuje automaticky k aktuální revizi. Podrobnosti obsahuje [kontrolní seznam](QA_RELEASE_CHECKLIST.md).

## Orientace v repozitáři

| Soubor nebo složka | Účel |
|---|---|
| [index.html](index.html) | Stránka, její styly a chování. |
| [assets](assets/) | Obrázky a hotové PDF. |
| [src](src/) | Obsah průvodce a jeho generátor. |
| [ai-log](ai-log/) | Přehled práce, historický přepis a označená redakční revize pokynů. |
| [CRO_FUNNEL_SPEC.md](CRO_FUNNEL_SPEC.md) | Aktuální konverzní cesta a hypotézy měření. |
| [QA_RELEASE_CHECKLIST.md](QA_RELEASE_CHECKLIST.md) | Rozsah ověření, důkazy a neprovedené kontroly. |
| [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) | Historie designových rozhodnutí; nejnovější stav shrnuje tento README. |
| [screenshots](screenshots/) | Starší snímky průběžných verzí, nikoli doklad současného zobrazení. |
| [CLAUDE_MASTER_PROMPT.md](CLAUDE_MASTER_PROMPT.md), [DESIGN_REFERENCE_LOCK.md](DESIGN_REFERENCE_LOCK.md), [FINAL_QUALITY_GATE.md](FINAL_QUALITY_GATE.md) | Původní pracovní podklady; nejsou prohlášením, že všechny požadavky byly splněny. |

Repozitář má jednu větev `main`. Změny v historii zachycují postupné zpracování; nejde o několik souběžných variant. Historie nebyla zpětně přepisována.

## Spuštění a obnova PDF

Web lze otevřít jako `index.html` nebo spustit místním statickým serverem. Nasazení používá Vercel bez sestavovacího kroku.

Obsah průvodce je v `src/pruvodce.html`, generátor v `src/build_pruvodce.py`. Vyžaduje Python 3, balíčky reportlab a beautifulsoup4 a písma Arial z macOS. Spuštění: `python3 src/build_pruvodce.py`.

## Před skutečnou kampaní

Doplnit ověřené údaje emitenta a emise, emisní dokumentaci a podklady k zajištění, právní posouzení, informace o zpracování údajů, vhodné fotografie, skutečné zpracování kontaktů a doručování. Měření má sledovat skutečně doručené a dosažitelné kontakty, poradcem přijaté zájemce, investice a cenu za investora. Analytika není nasazená; obchodní výkon je hypotéza.

## Použití AI

První verze vznikla s ChatGPT, další zpracování s Claude Code a závěrečná revize s Codexem. [Přehled postupu](ai-log/POSTUP-A-ROZHODNUTI.md) propojuje rozhodnutí s historií změn. [Historický přepis](ai-log/claude-code-export.txt) je převedený, zkrácený a anonymizovaný záznam; není doslovným výstupem `/export`. Dodatečně upravené formulace jsou oddělené od původního přepisu.

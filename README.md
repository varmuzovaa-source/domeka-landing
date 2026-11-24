# Domeka — ukázková investiční landing page

**Živá stránka:** https://domeka-landing.vercel.app · **Repozitář:** https://github.com/varmuzovaa-source/domeka-landing

Fiktivní klient a fiktivní dluhopis, vytvořeno pro praktický úkol (Junior AI Developer). Statický web v češtině: HTML, CSS a trocha JavaScriptu, bez knihoven, bez backendu, bez externích požadavků.

- Vstup: `index.html`, fotografie v `assets/` (úvodní fotografie a nádvoří před opravou)
- Rozhodnutí: `DESIGN_DECISIONS.md`, `DESIGN_REFERENCE_LOCK.md`
- Funnel a hypotézy: `CRO_FUNNEL_SPEC.md` a sekce níže
- QA: `QA_RELEASE_CHECKLIST.md`, `screenshots/`
- AI log: `ai-log/README.md`

## Shrnutí pro hodnotitele
- **Lead magnet:** „Pět otázek před nákupem firemního dluhopisu“, dvě strany A4 s otázkami, kde hledat odpověď, ukázkovým výpočtem výplat a dotazy na poradce.
- **Kdy žádám o kontakt:** až po vysvětlení produktu, výpočtu a rizik a po dvou krátkých otázkách (částka, horizont). Po kvalifikaci je potřeba e-mail; zájemce o konzultaci může místo něj uvést telefon.
- **Co povede ke konverzi:** úvodní část říká totéž co reklama (dluhopis, od 50 000 Kč, 4 roky, čtvrtletní úrok), ukazuje konkrétní výpočet a otevřeně mluví o rizicích.
- **Jak magnet ovlivní kvalitu kontaktů:** dvě otázky před kontaktem rozliší deklarovanou částku a termín investice. Poradce se nabízí jen první skupině.
- **Naměřeno (Lighthouse, mobil, živá URL):** výkon 99, přístupnost 100, doporučené postupy 100, SEO 100.

## Cíl
Ne maximum formulářů, ale co nejvíc lidí, kteří rozumějí podmínkám a rizikům a mohou skutečně investovat alespoň 50 000 Kč. Proto web nejprve vysvětluje, až potom se ptá, a kontakt žádá až po ukázce hodnoty průvodce a dvou otázkách.

## Cesta zájemce (funnel)
Reklama (slib: „Jak může fungovat čtyřletý dluhopis financující obnovu bytových domů?“) → úvodní část se stejným slibem → podmínky a vysvětlení → rizika → lead magnet → dvě otázky bez kontaktu → výsledek podle odpovědí → e-mail nebo telefon pro konzultaci → (v ostrém provozu) konzultace → případná investice.

**Lead magnet:** „Pět otázek před nákupem firemního dluhopisu“. Konkrétní rozhodovací pomůcka (kontrolní seznam, ukázkový výpočet výplat, otázky na poradce), ne obecný e-book. Je vyrobený jako dvoustránkové PDF ke stažení (`assets/Domeka-Pet-otazek-pred-nakupem-dluhopisu.pdf`, zdroj v `src/pruvodce.html`).

**Proč kontakt až teď:** člověk 50+ s dluhopisy nezačíná e-mailem. Nejprve musí vidět, co kupuje a co riskuje. Průvodce má pro něj reálnou hodnotu i tehdy, když nakonec neinvestuje, a proto je ochotnější o něj požádat. Dvě otázky rozliší deklarovanou částku a termín. Samy neprokazují schopnost investovat ani vhodnost investice; použitelný kontakt v ostrém provozu vzniká až doručením dosažitelného spojení. PDF se v rozhraní zpřístupní až po jeho vyplnění. Je to hypotéza, kterou by ověřil A/B test (níže).

### Větvení formuláře (otestováno, viz QA)
| Odpovědi | Výsledek | Nabídka poradce |
|---|---|---|
| ≥ 50 000 Kč a „v příštích 3 měsících“ | Předběžně kvalifikovaný zájemce | Ano; e-mail nebo telefon pro požadovanou konzultaci |
| ≥ 50 000 Kč a „sbírám informace / později / nevím“ | Vzdělávací kontakt | Ne |
| „Méně než 50 000 Kč“ | Pod minimem, nepočítá se jako kvalifikovaný | Ne |
| „Zatím zjišťuji“ | Informační kontakt | Ne |

Texty představují modelovou nabídku. Fiktivní povaha projektu je přiznaná v patičce i PDF. Formulář nemá backend: nic neodesílá ani neukládá (zadání to dovolovalo); před kontaktními poli i po dokončení je to výslovně uvedeno. Bez kontaktu formulář dokončit nelze. E-mail je výchozí cesta; u nabídky konzultace ho může nahradit platný telefon. Po dokončení se zobrazí stažení PDF, bez skutečného doručení či uložení kontaktu. Před ostrým spuštěním je nutné napojit ho na e-mailovou službu a CRM.

### Dva příklady návštěvy
- **Investor 50+, 100 tis. Kč:** přečte podmínky a rizika, v průvodci zvolí „100 000–499 999 Kč“ a „v příštích 3 měsících“, dostane výsledek „Možný zájem o konzultaci“ a může zaškrtnout kontakt poradce. Pro obchodní tým je to prioritní kontakt, vždy s ověřením vhodnosti.
- **Člověk s 20 tis. Kč:** zvolí „Méně než 50 000 Kč“, dostane vysvětlení, že minimum je 50 000 Kč, a obecnou pomůcku. Poradce se mu nenabízí. Má férovou cestu, ale není započítán jako kvalifikovaný.

## Fiktivní a doplněné údaje
Ze zadání: zajištění domy firmy, pevný úrok vyplácený čtvrtletně, splatnost 4 roky, minimum 50 000 Kč, cíl emise 150 mil. Kč.

Doplněno a **fiktivní**:
- sazba **7,2 % p. a.** (modelový předpoklad, na 50 000 Kč to je 3 600 Kč ročně, 900 Kč čtvrtletně, 14 400 Kč za 4 roky před zdaněním; není to slib výplaty),
- jméno emitenta Domeka a popis podnikání,
- lead magnet a kvalifikační otázky,
- modelový nájem 14 000 Kč a z něj spočtených 65 plně pronajatých bytů (900 000 / 14 000 = 64,286, zaokrouhleno nahoru; jejich hrubé nájemné pokrývá pouze úroky, bez nákladů a splacení jistiny),
- údaje o firmě: činnost od roku 2012, 46 opravených domů, ≈ 520 pronajatých bytů, obsazenost 97 %, zástava domů, ocenění soudním znalcem, nezávislý správce zajištění, upisování do 31. 3. 2027,
- kontakt a adresa v patičce (`investori@domeka.cz`, Praha 8 – Karlín, Po–Pá 9–17),
- kalkulačka výnosu v úvodu (sazba 7,2 % p. a.) a PDF průvodce,
- fotografie: dva ilustrační snímky vytvořené umělou inteligencí. Nezobrazují nemovitosti Domeky, což říká patička. Před ostrým spuštěním je nahradit licencovanými fotografiemi.

Žádné reference, ocenění, počty investorů, loga regulátorů ani pojišťoven.

## CRO hypotézy pro skutečný provoz (ne naměřené výsledky)
1. **Úvodní část:** „4 roky / čtvrtletní výplata“ proti „obnova bytových domů“. Měřit qualified lead rate a podíl financovaných investorů spolu s kontrolou porozumění rizikům.
2. **Pořadí formuláře:** dvě otázky před e-mailem proti e-mailu první. Měřit počet poradcem přijatých kontaktů na 100 kliků, nejen surovou konverzi.
3. **Rámování magnetu:** „Pět otázek před nákupem“ proti „Dluhopis jednoduše“. Měřit přechod od stažení k smysluplnému rozhovoru a porozumění rizikům.

Metriky: qualified lead rate, cost per qualified lead, contact-to-investor rate, cost per funded investor.

## Co před ostrým spuštěním chybí
Emisní podmínky, prospekt nebo výjimka a povinná sdělení, skutečná sazba a zajištění, údaje o emitentovi a dokumenty, licencované fotografie místo AI ilustrací, informace o zpracování osobních údajů a právní základ, funkční odeslání kontaktu a případné doručení průvodce e-mailem (přímé stažení PDF funguje), evidence souhlasů, CRM a právní kontrola.

## Spuštění
Otevřete `index.html`, nebo `python3 -m http.server`. Nasazení: libovolný statický hosting, například Vercel (bez build příkazu, kořen projektu).

## AI log
Viz `ai-log/README.md`. První verzi vytvořil ChatGPT, redesign a nasazení provedl Claude Code. V `ai-log/claude-code-export.txt` je upravený textový přepis relace Claude Code, nikoli doslovný výstup příkazu `/export` (vznikl z oficiálního exportu relace, výsledky čtení Gmailu jsou vypuštěny, protože obsahovaly soukromé e-maily třetích osob). Původní poznámka o ChatGPT je zachovaná.

## Revize po Claude Code — 24. 11. 2026
Jazykovou, marketingovou a technickou revizi následně provedl Codex. Nemění historický záznam práce v Claude Code. Aktuální ověření a limity jsou v QA_RELEASE_CHECKLIST.md; starší měření Lighthouse výše se nevztahuje automaticky k této revizi.

Zachováno: statický HTML/CSS/JavaScript bez knihoven a bez ukládání kontaktů. Jemný pohyb pouze jako odezva tlačítek a kalkulačky; respektuje omezení pohybu. Designový směr zachován.

Měření pro ostrý provoz (zatím nenasazeno): návštěva → otevření otázek → dokončení otázek → stažení PDF → skutečně doručený a dosažitelný kontakt → poradcem přijatý kontakt → investice. Kvalifikace podle částky a termínu není potvrzením vhodnosti. Do analytiky neposílat e-mail ani telefon. Úspěch kontaktu měřit až po potvrzeném doručení, ne kliknutím na tlačítko.

## Lead magnet — konečná cesta schválená Andreou
Cílem je získat e-mail, ideálně od člověka s částkou alespoň 50 000 Kč; telefon je alternativou u zájmu o konzultaci. Náhled průvodce je veřejný, hotové PDF je v uživatelské cestě až za kontaktem. Dvě otázky před kontaktem rozlišují částku a termín; lidem pod minimem zůstává vzdělávací cesta za e-mail bez nabídky hovoru. E-mail a telefon současně nevyžadujeme.

Jde o ukázku pro výběrové zadání, nikoli skutečný sběr kontaktů. Proto se používají testovací údaje a výsledek nepředstírá odeslání. Odkaz na PDF v patičce i před kontaktním krokem byl odstraněn. Statický soubor v assets však není zabezpečený: kdo zná jeho adresu, může jej otevřít přímo. Pro skutečně řízené doručování je potřeba serverová kontrola, uložení kontaktu a odeslání nebo dočasný odkaz.

## Obnovení PDF
Obsah: src/pruvodce.html. Generátor: src/build_pruvodce.py (Python 3, reportlab, beautifulsoup4; písma Arial z macOS). Spuštění: python3 src/build_pruvodce.py. PDF má dvě strany; aktuální soubor byl po přegenerování vizuálně zkontrolován.

> Původní pracovní zadání pro Claude Code, zachované pro kontext. Není potvrzením aktuálního chování ani splnění všech požadavků. Aktuální řešení popisují [README](README.md) a [konverzní cesta](CRO_FUNNEL_SPEC.md); provedené kontroly a chybějící přímý export uvádí [kontrolní seznam](QA_RELEASE_CHECKLIST.md).

# CLAUDE CODE — DOMEKA / SENIOR PRODUCT DESIGN + CRO + FRONTEND ENGINEERING

Jsi současně seniorní product designer, creative director zaměřený na high-trust fintech, CRO strategist, senior frontend engineer a QA reviewer. Pracuješ přímo v TOMTO otevřeném projektu Domeka. Nezačínej od nuly bez přečtení existujícího `index.html`, `README.md`, `DESIGN_REFERENCE_LOCK.md`, `QA_RELEASE_CHECKLIST.md` a `ai-log/README.md`.

## 0 / Kontext, skutečný cíl a omezení

Jde o praktický úkol pro Junior AI Developer — nikoli o produkční finanční nabídku. Fiktivní firma DOMEKA kupuje starší bytové domy, rekonstruuje je a následně pronajímá byty. Pro fiktivní emisi chce získat 150 mil. Kč. Dluhopis je dle zadání zajištěný domy firmy, má pevný úrok vyplácený čtvrtletně, splatnost 4 roky a minimální investici 50 000 Kč. Hlavní návštěvník: český drobný investor 50+, který dosud dluhopis nekoupil, přichází z mobilní reklamy a během pár sekund se rozhoduje, zda pokračuje.

Není cílem maximální počet náhodných leadů. Skutečná obchodní metrika je počet lidí, kteří nakonec investují ALESPOŇ 50 000 Kč. Funnel proto musí zároveň vzdělávat, budovat důvěru a citlivě kvalifikovat, bez klamání nebo agresivního nátlaku.

Termín odevzdání: 24. 11. 2026 do konce dne. Zadavatel očekává: veřejnou URL, několik vět proč konkrétní lead magnet a kdy se žádá kontakt, konverzní argumentaci, veřejné GitHub repo a `ai-log/` se SKUTEČNÝM exportem konverzace Claude Code přes `/export`.

K dispozici je existující statický HTML/CSS/JS projekt. Zachovej jednoduchost a nulové nebo minimální hostingové náklady. Formulář dle zadání NEMUSÍ posílat data do backendu. Nesmí však předstírat, že skutečný e-mail byl odeslán nebo že PDF reálně existuje.

## 1 / Nejdřív výzkum, pak design (POVINNÉ)

Použij Refero skill / MCP, pokud je k dispozici. Připojení dle potřeby:
`claude mcp add --transport http refero https://api.refero.design/mcp`
Potom `/mcp` a případná autorizace. Pokud MCP není funkční, použij již připravený `DESIGN_REFERENCE_LOCK.md`; netvrď, že jsi provedl nové hledání.

Reference už byly vyhodnocené pomocí Refero:
- **Aker / akercompanies.com**: PRIMÁRNÍ vizuální základ. Architektonická fotografie jako důkaz předmětu podnikání; bílý canvas, tmavě ocean/forest tón, jemné předěly, přehledné číslice a disciplína kolem důvěry.
- **Public / public.com**: SEKUNDÁRNÍ pro informační hierarchii finančního produktu, jasný CTA a strukturovaná vysvětlení. Nepřebírej složité animace nebo technický cyan jako značkovou barvu.
- **Titan / titan.com**: SEKUNDÁRNÍ pro klidný institucionální rytmus, kvalitní editorial spacing a kompaktní konverzní akce. Nekopíruj corporate fotografický styl ani ivory generický vzhled.

Vytvoř krátký audit existující stránky a seznam rozhodnutí, co převzít, v čem se odchýlit a proč. Žádné vizuální rozhodnutí bez zdroje: reference / uživatelský brief / přístupnost / skutečné použití.

## 2 / Požadovaný vizuální výsledek

Dodej design, který působí jako práce zkušeného digitálního studia pro investice do nemovitostí: atraktivní, přesný, klidný, současný, zřetelně profesionální. Cílovka 50+ není důvod pro zastaralý vzhled; znamená to čitelnou typografii, důvěryhodný obsah, vysoký kontrast a velká dotyková místa.

Směr: **architecture-led investment editorial**. Primární barevnost bílá / lehce studená šedá, ink/charcoal, velmi tmavá petrolejová nebo forest zelená, jediný disciplinovaný CTA akcent. Zachovej konzistentní použití barev podle rolí. Typografie: přirozeně čitelný sans (např. Inter/Manrope); případný display serif jen pokud jej Refero opodstatní, ale nedělej typický AI design s náhodnou kurzívou v jednom slově. Jasná vizuální hierarchie; jednotné mezery, radius, border, states, design tokens. Žádný glassmorphism, křiklavé gradienty, levné ikonky, falešné statistiky ani tři generické benefit karty jen do počtu.

**Nejslabší současný prvek je CSS pseudoilustrace bytového domu.** Nahradit kvalitní, právně použitelnou architektonickou fotografií staršího městského bytového domu nebo konkrétním před/po vizuálním konceptem. Pokud není ověřený licenční asset, použij dobře označený vizuální placeholder a art direction; nevymýšlej referenční stavby nebo projekty firmy. Nepoužívej vymyšlené portréty týmu či „klientské recenze“. Když je asset externí, ošetři fallback, lazy loading, alt a aspect ratio; ideálně uložit lokálně licencovaný soubor do `assets/`.

Na mobilu 375 px musí první viewport říct: **co je to za nabídku / od kolika / na jak dlouho / co má uživatel udělat**. Hero nemá být jen obří slogan. Na desktopu využij prémiovou asymetrii text/obraz. Sticky CTA lze použít jen decentně a nesmí zakrývat obsah, formulář či právní upozornění.

## 3 / CRO a informační architektura

Navrhni optimalizovanou sekvenci:
A. Hero: důvěryhodný a konkrétní headline, stručný subheadline vysvětlující princip, 1 primární CTA typu „Zjistit podmínky a získat přehled“, 1 měkká cesta „Jak dluhopis funguje“. Nad foldem podmínky: od 50 000 Kč, 4 roky, pevný čtvrtletní kupon; neprezentuj neověřené zajištění jako garanci bezpečí.
B. Přehled modelových podmínek pod hero, ale vždy s kontextem a odpovídajícím označením modelových parametrů.
C. Jak investice / investiční mechanismus funguje v jednoduché časové lince či diagramu srozumitelném pro člověka bez zkušenosti s dluhopisy; rozdíl oproti bankovnímu vkladu.
D. Co musí návštěvník vědět o zajištění a rizicích — jasně, bez skrývání nebo dramatizace.
E. Lead magnet: **„Pět otázek před nákupem firemního dluhopisu“** (alternativa „Dluhopis bez složité řeči“). Nejde o prázdný generický ebook, ale o užitečnou jednu až dvě strany: vysvětlení zajištění, co porovnat, jak číst podmínky, co se poradce zeptat, jednoduchý ukázkový výpočet cashflow. Tuto příručku není třeba reálně vyrobit; neslibuj, že je již možné ji stáhnout.
F. Kvalifikační krok: indikace investičního pásma (`zatím zjišťuji`, `<50 000 Kč`, `50–100 000 Kč`, `100–500 000 Kč`, `500 000 Kč+`) a časový horizont. Zvaž dvě fáze formu: 1) dvě rychlé otázky bez kontaktu, 2) e-mail pro průvodce; telefon volitelně, nikoliv skrytě povinný. Zjisti, zda je výhodnější požádat o e-mail před kvalifikací: napiš hypotézu a trade-off, vyber variantu s lepším poměrem kvalita kontaktu × friction. Člověk pod 50 tisíc nemá být falešně slibován jako investičně vhodný lead, ale může dostat vzdělávací obsah.
G. FAQ orientované na obavy: komu peníze půjčuji, co je zástava, co když emitent neplatí, předčasné vystoupení, zda je to pojištěný vklad.
H. Poslední CTA po zodpovězení námitek, ale bez nátlaku a countdownů.

Uvažuj jako growth marketer: od reklamy (hlavní promise) přes landing page až ke kvalifikačnímu callu. Popiš 2-3 hypotézy A/B testů (hero důraz, pořadí formuláře, lead magnet framing). Neoptimalizuj na prostý conversion rate, ale na qualified-lead rate / contact-to-investor rate, případně cost per funded investor. Žádné vymyšlené výsledky.

## 4 / Finanční a regulatorní přesnost

Zadání výslovně dovoluje věrohodně doplnit chybějící údaje, ale musíš je uvést v README a v předávacím e-mailu. Navrhuji *výhradně pro demonstraci* pevný kupón 7,2 % p. a. a čtvrtletní výplatu. Na modelových 50 000 Kč by to matematicky bylo 900 Kč za čtvrtletí před případným zdaněním, při řádném plnění emitenta. **Nejde o garantovaný výnos ani ověřený reálný produkt.** Pokud sazbu použiješ, umísti ji v dostatečném kontextu s nejistotou splnění závazků. Nemíchej modelové údaje s ověřenými fakty.

„Zajištěný nemovitostmi“ neznamená „bezpečný“: zajištění závisí na zástavním právu, hodnotě, pořadí zástavy, dispozicích nemovitostmi a na vymahatelnosti. Bez emisních podmínek nemá smysl tvrdit konkrétní LTV, nadřazenost pohledávky, výši zajištění ani historii výnosů. Výrazná, avšak dobře integrovaná informace „FIKTIVNÍ UKÁZKA / NENÍ NABÍDKA INVESTICE“ musí být trvale čitelná. Žádné falešné schvalovací značky ČNB, fiktivní audit, reference, recenze, počty investorů ani sliby návratnosti. Odborně překontroluj češtinu a terminologii; veškerý obsah v češtině pro českého investora.

Pro testovací projekt je funkční UI simulace formuláře v pořádku, ale jasně zobraz, že nic neposílá. Žádné prázdné privacy policy linky ani lživý souhlas. V reálném provozu by bylo nutné právní/compliance posouzení, doložení emitenta a dokumentů a funkční privacy/CRM; explicitně odliš v README. Nepracuj s osobními údaji jako by byly skutečně uložené.

## 5 / Technická realizace a QA

Preferuj vylepšit stávající statické řešení HTML/CSS/JS a komponentizovat jen pokud to opravdu zlepší kvalitu nebo udržitelnost. Nepřepisuj na Next.js bez důvodu. Kód má být čitelný, mobile-first a bez nepotřebných závislostí. Dodrž WCAG základy: label/input, kontrast, focus-visible, klávesnice, aria-live validace, 44 px touch target, reduced-motion, semantic sections. Testuj 320 / 375 / 390 / 768 / 1024 / 1440 px. Zkontroluj overflow, typografické přelomy, sticky prvky, FAQ, formulář a stav po submitu. Proveď reálné screenshoty přes Playwright/browser pokud lze a vizuální kontrolu po každé větší změně. Žádná falešná tvrzení o testech, které neproběhly.

Výstupy:
1. Upravený produkčně vypadající `index.html` (+ lokální `assets/`, pokud jsou použity).
2. `README.md` s výčtem fiktivních parametrů, popisem funnelu, lead magnetu, CRO hypotéz, tech stackem a limity demo.
3. `QA_RELEASE_CHECKLIST.md` se skutečně ověřenými / neověřenými kontrolami.
4. Připravené nasazení na bezplatný Vercel hosting a veřejný GitHub repo; pokud nemáš autorizaci, explicitně vypiš jediný další ruční krok, nic si nevymýšlej.
5. Skutečný export TÉTO konverzace z Claude Code přes `/export` uložený do `ai-log/`. Pokud export nejde automaticky, dej jasný návod, nefalšuj jej a NEODSTRAŇ původní poznámku o použití ChatGPT.
6. Závěrečná zpráva: změny, proč zlepší pravděpodobnost kvalitních leadů, konkrétní URL pouze pokud ověřena, QA a přesný seznam zbývajících blokátorů.

## 6 / Pracovní postup – udělej bez čekání na moje schválení

KROK 1 Audit: vypiš 8–12 nejdůležitějších problémů současného webu; rozliš vizuál, UX, konverze, regulaci a techniku.
KROK 2 Refero: vytvoř `DESIGN_DECISIONS.md` s reference lock a nejdůležitějšími tokeny. Přidej 2–3 varianty hero/headline krátce, vyber vítěznou podle cílové skupiny a pokračuj. Nečekej na mě.
KROK 3 Implementace: celý redesigned web s profesionálním vizuálem, ne jen seznam doporučení.
KROK 4 Testy: mobil/desktop, validace, accessibility, úprava nalezených problémů.
KROK 5 Odevzdání: README + QA + ai-log export + návrh stručného e-mailu zadavateli. Nic mu neodesílej bez mého potvrzení.

Nešetři péči na první obrazovce mobilu, architektonickém hero vizuálu a funnelu. Cílem je stránka, kterou bych jako seniorní marketérka bez rozpaků ukázala vedení, a která nevyhlíží jako výchozí Claude/Lovable šablona.

## 7 / Konverzní logika navíc (POVINNÉ)

Přečti `CRO_FUNNEL_SPEC.md` a implementuj jeho doporučení. Dvoufázový formulář může být jednoduchý, ale musí skutečně pracovat s odpověďmi a mít jasné stavy pro (a) potenciálně kvalifikované investory, (b) zájemce pod minimem, (c) ty, kteří jen sbírají informace. Nezaměňuj e-mailový lead za dokončenou investici. U demo formuláře nevytvářej falešný úspěšný stav o zaslání materiálů. Otestuj toto větvení ručně nebo automatizovaně a zaznamenej skutečný výsledek.

Po opravách dej dvě krátké příklady návštěvy: investor 50+ připravený vložit 100 tis. Kč a člověk s 20 tis. Kč. Ukaž, proč oba mají férovou uživatelskou cestu, ale nejsou stejně kvalifikovaní pro obchodní tým.

## 8 / Finální kontrola kvality — povinná
Přečti a splň `FINAL_QUALITY_GATE.md`. Na závěr dolož skutečné screenshoty, konkrétní výsledky testů a pravdivý stav GitHub/Vercel/Claude /export. Nic nepředstírej a nezastavuj se u návrhu doporučení — proveď implementaci.

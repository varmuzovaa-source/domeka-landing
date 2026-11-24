# DOMEKA — audit, reference lock a designová rozhodnutí

Datum: 24. 11. 2026. Fiktivní klient, fiktivní dluhopis.

## 1. Audit původní stránky (v3 handoff, 8 nejdůležitějších problémů)

| # | Oblast | Problém | Řešení |
|---|---|---|---|
| 1 | Vizuál | Hlavní obraz byl CSS pseudoilustrace domu s gradienty, působila jako šablona. | Celoplošná fotografie opravené bytový fasády (AI ilustrace, označená v patičce), druhá fotografie nádvoří před opravou. Bez popisků pod obrázky. |
| 2 | Vizuál | Plovoucí karta přes obraz, stíny, fixní odznak, zelenobéžová paleta s limetkou. | Plochý povrch, čáry místo stínů, jedna CTA barva (ocean `#123D44`). |
| 3 | Mobil / UX | Hero na 375 px nedával dohromady produkt, minimum, dobu a další krok. | H1, 4 podmínky ve 2×2 mřížce a CTA jsou v prvním viewportu. |
| 4 | Konverze | Kvalifikační formulář byl jeden blok s povinným e-mailem a bez větvení. | Dvoukrokový funnel. Dvě otázky bez kontaktu, potom čtyři různé výsledky a nepovinný kontakt. |
| 5 | Konverze | Lead magnet byl „ebook“ bez konkrétní hodnoty. | „Pět otázek před nákupem firemního dluhopisu“ s viditelným náhledem všech pěti otázek. |
| 6 | Regulace | Tvrzení o zajištění a výnosu bez kontextu, bez ilustrace výpočtu. | Riziko přímo u hero, samostatná sekce rizik, modelová sazba všude označená jako fiktivní. |
| 7 | Regulace | Formulář tvrdil „zaslání průvodce“, které by nenastalo. | Po dokončení výslovně: údaje se neodesílají, průvodce se neposílá. Žádná data se neukládají. |
| 8 | Technika / přístupnost | Barevný kontrast, malá písma (~13 px), `select` místo radií, fixní badge, Google Fonts bez nutnosti. | Základ 17–18 px, radia 52 px, focus-visible, aria-live, `prefers-reduced-motion`, žádné externí požadavky. |

## 2. Reference lock (Refero, 23.–24. 11. 2026)

Výzkum 23. 11. je v `DESIGN_REFERENCE_LOCK.md`. Dne 24. 11. jsem znovu ověřil, že Refero MCP funguje, a načetl plný styl Aker (`9b254d6b-c287-43f0-bdc3-99f61afbdac1`). Vyhledal jsem také vzory vícekrokových formulářů s volbou částky (Wealthsimple: radia v jednom sloupci, stručný krok, jedna akce).

| Zdroj | Co přebírám (jako princip) | Čemu se vyhýbám |
|---|---|---|
| **Aker** (primární) | Bílé plátno, jemná linka místo karet, „ledger“ s indexy, velká lehká čísla, jeden tmavý kapitolový blok, radius 8 px, ocean `#002934` jako role tmavé kapitoly. | Full-bleed film, glass karty, serif Lora. Neexistuje licencovaná fotografie. |
| **Public** (sekundární) | Pořadí vysvětlení finančního produktu, srozumitelná CTA. | Tmavé technické panely, cyan. |
| **Titan** (sekundární) | Klidný rytmus, pilulková tlačítka. | Korporátní fotky, béžový vzhled. |
| **Wealthsimple** (jen formulář) | Jedna otázka = jedna skupina radií, bez rozptýlení. | Navigační lišta aplikace. |

Žádné vizuální rozhodnutí není bez zdroje: reference, zadání, přístupnost, nebo reálné použití.

**MotionSites:** účet je na free plánu, premium prompty jsou zamčené. Nalezené návrhy (Luxury Real Estate, Investment Gate) jsou animované video šablony, které by narušily uzamčený směr, proto jsem je nepoužil.

## 3. Varianty hero a vítěz

| Varianta | H1 | Posouzení pro 50+ |
|---|---|---|
| A | „Starým domům nový začátek. Vašim penězům jasný plán.“ (původní) | Sloganový, neřekne produkt. Slibuje „jasný plán“. Zamítnuto. |
| B | „Čtyři roky. Čtvrtletní úrok. Od 50 000 Kč.“ | Konkrétní, ale chladný a zdůrazňuje výnos. Vhodné do A/B testu. |
| **C (vítěz)** | „Dluhopis na obnovu bytových domů“ + „Nejprve porozumět. Potom se rozhodnout.“ | Pojmenuje produkt, shoduje se s reklamou i spec. `CRO_FUNNEL_SPEC.md`, nenatlačuje. |

## 4. Tokeny

- Barvy: canvas `#FFFFFF`, support `#F4F6F6`, text `#16242A`, muted `#4E5D63`, linka `#DCE3E3`, ocean `#123D44` (CTA a jedna tmavá kapitola), signal `#C4E4DE` (jen drobné popisky na tmavé), varování `#7A4B00` jen u štítku „fiktivní“.
- Typografie: Inter / systémový sans. H1 váha 500, tracking −0,03 em, tělo 17 px (18 px od 768 px).
- Mezery: sekce 64 px / 96 px, okraje 20 px / 32 px, max šířka 1200 px.
- Prvky: tlačítka min. 52 px, pilulka; radio 52 px; radius 8 px; stíny žádné.
- Kontrasty (spočítáno podle WCAG): text/bílá 15,9:1, muted/bílá 6,8:1, muted/support 6,3:1, bílá/ocean 11,8:1, signal/ocean 8,7:1, varování/žlutý štítek 6,8:1, chyba/bílá 8,3:1. Všechny splňují AA (4,5:1).

## 5. Placeholder fotografie: art direction

Do `assets/` patří licencovaná fotografie staršího městského bytovýho domu (3–5 podlaží), frontální nebo mírně šikmý pohled, přirozené denní světlo, bez lidí a značek, poměr 4:5 desktop / 4:3 mobil. Titulek musí zůstat: „Ilustrační fotografie. Nejde o nemovitost společnosti Domeka.“ Fotografii nevydávat za majetek emitenta.


## 6. Redesign 24. 11. (odpoledne)

Původní verze s výkresem působila slabě. Změny: celoplošný hero s fotografií a směrovým stínováním (text vlevo), velká typografie, čísla v „ledgeru“ místo karet, sekce „Z čeho se platí“ s konkrétním výpočtem (úroky z 150 mil. Kč = 900 000 Kč měsíčně = ≈ 64 pronajatých bytů při modelovém nájmu 14 000 Kč), náhled první strany průvodce, mezi-CTA po výpočtu a mobilní lišta s odkazem na průvodce (skrývá se u formuláře). Texty jsou konkrétní a vycházejí z čísel, ne z obecných slibů. Taste skill: bez popisků pod obrázky, jedna sekce = jedna myšlenka, stejné okraje, hover odezva tlačítek.

## 7. Úprava po zpětné vazbě

Fotografie interiéru byla vyřazena, protože do příběhu nezapadala. Sekce „Co kupujete“ je nově text a ledger, doplněný srovnáním „Co dostanete / Co přebíráte vy“. Texty jsou přepsané copywriterským tónem: konkrétní čísla, přímé oslovení a poctivé vyvážení výhod a rizik.

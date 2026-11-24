# Domeka — ukázková investiční landing page

Fiktivní klient a fiktivní dluhopis, vytvořeno pro praktický úkol (Junior AI Developer). Statický web v češtině: HTML, CSS a trocha JavaScriptu, bez knihoven, bez backendu, bez externích požadavků.

- Vstup: `index.html`, obraz `assets/hero-placeholder.svg`
- Rozhodnutí: `DESIGN_DECISIONS.md`, `DESIGN_REFERENCE_LOCK.md`
- Funnel a hypotézy: `CRO_FUNNEL_SPEC.md` a sekce níže
- QA: `QA_RELEASE_CHECKLIST.md`, `screenshots/`
- AI log: `ai-log/README.md`

## Cíl
Ne maximum formulářů, ale co nejvíc lidí, kteří rozumějí podmínkám a rizikům a mohou skutečně investovat alespoň 50 000 Kč. Proto web nejdřív vysvětluje, až potom se ptá, a kontakt je nepovinný.

## Funnel
Reklama (slib: „Jak může fungovat čtyřletý dluhopis financující obnovu bytových domů?“) → hero se stejným slibem → podmínky a vysvětlení → rizika → lead magnet → dvě otázky bez kontaktu → výsledek podle odpovědí → nepovinný kontakt → (v ostrém provozu) konzultace → případná investice.

**Lead magnet:** „Pět otázek před nákupem firemního dluhopisu“. Konkrétní rozhodovací pomůcka (kontrolní seznam, ukázkový výpočet výplat, otázky na poradce), ne obecný e-book. V ukázce je navržený, ale **není vyrobený ke stažení**.

**Proč kontakt až teď:** člověk 50+ s dluhopisy nezačíná e-mailem. Nejdřív musí vidět, co kupuje a co riskuje. Průvodce má pro něj reálnou hodnotu i tehdy, když nakonec neinvestuje, a proto je ochotnější o něj požádat. Dvě otázky před e-mailem odliší záměr od zvědavosti, takže obchodní tým nedostane stovky kontaktů pod minimem. Je to hypotéza, kterou by ověřil A/B test (níže).

### Větvení formuláře (otestováno, viz QA)
| Odpovědi | Výsledek | Nabídka poradce |
|---|---|---|
| ≥ 50 000 Kč a „v příštích 3 měsících“ | Kvalifikovaný kontakt | Ano, nepovinný souhlas a telefon |
| ≥ 50 000 Kč a „sbírám informace / později / nevím“ | Vzdělávací kontakt | Ne |
| „Méně než 50 000 Kč“ | Pod minimem, nepočítá se jako kvalifikovaný | Ne |
| „Zatím zjišťuji“ | Informační kontakt | Ne |

Formulář nikam nic neposílá ani neukládá a po dokončení to výslovně říká. Zobrazí jen, jak by kontakt zařadil CRM.

### Dvě příklady návštěvy
- **Investor 50+, 100 tis. Kč:** přečte podmínky a rizika, v průvodci zvolí „100–500 000“ a „v příštích 3 měsících“, dostane výsledek „Možný zájem o konzultaci“ a může zaškrtnout kontakt poradce. Pro obchodní tým je to prioritní kontakt, vždy s ověřením vhodnosti.
- **Člověk s 20 tis. Kč:** zvolí „Méně než 50 000 Kč“, dostane vysvětlení, že minimum je 50 000 Kč, a obecnou pomůcku. Poradce se mu nenabízí. Má férovou cestu, ale není započítán jako kvalifikovaný.

## Fiktivní a doplněné údaje
Ze zadání: zajištění domy firmy, pevný úrok vyplácený čtvrtletně, splatnost 4 roky, minimum 50 000 Kč, cíl emise 150 mil. Kč.

Doplněno a **fiktivní**:
- sazba **7,2 % p. a.** (modelový předpoklad, na 50 000 Kč to je 3 600 Kč ročně, 900 Kč čtvrtletně, 14 400 Kč za 4 roky před zdaněním; není to slib výplaty),
- jméno emitenta Domeka a popis podnikání,
- lead magnet a kvalifikační otázky,
- hero vizuál (schematický výkres, placeholder za fotografii).

Žádné reference, ocenění, počty investorů, loga regulátorů ani pojišťoven.

## CRO hypotézy pro skutečný provoz (ne naměřené výsledky)
1. **Hero:** „4 roky / čtvrtletní výplata“ proti „obnova bytových domů“. Měřit qualified lead rate a podíl financovaných investorů spolu s kontrolou porozumění rizikům.
2. **Pořadí formuláře:** dvě otázky před e-mailem proti e-mailu první. Měřit počet poradcem přijatých kontaktů na 100 kliků, nejen surovou konverzi.
3. **Rámování magnetu:** „Pět otázek před nákupem“ proti „Dluhopis jednoduše“. Měřit přechod od stažení k smysluplnému rozhovoru a porozumění rizikům.

Metriky: qualified lead rate, cost per qualified lead, contact-to-investor rate, cost per funded investor.

## Co před ostrým spuštěním chybí
Emisní podmínky, prospekt nebo výjimka a povinná sdělení, skutečná sazba a zajištění, údaje o emitentovi a dokumenty, licencovaná fotografie, informace o zpracování osobních údajů a právní základ, funkční doručení průvodce, evidence souhlasů, CRM a právní kontrola.

## Spuštění
Otevřete `index.html`, nebo `python3 -m http.server`. Nasazení: libovolný statický hosting, například Vercel (bez build příkazu, kořen projektu).

## AI log
Viz `ai-log/README.md`. První verzi vytvořil ChatGPT, redesign provedl Claude Code. Původní poznámka o ChatGPT je zachovaná. Export `/export` z Claude Code je třeba pořídit ručně a uložit do `ai-log/`.

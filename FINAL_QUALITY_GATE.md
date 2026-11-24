# Domeka — finální kvalitativní brána pro Claude Code

Tento soubor doplňuje `CLAUDE_MASTER_PROMPT.md`. Cílem není jen vizuálně hezké demo, ale přesvědčivý, poctivý mobilní funnel pro investora 50+ a obhajitelný výstup výběrového řízení.

## P0: bez splnění neodevzdávat

1. **Prvních 5 sekund na mobilu 375 px:** návštěvník musí rozumět tomu, že jde o dluhopis, minimum 50 000 Kč, splatnost 4 roky, fixní kupón čtvrtletně, a co udělat dál. Nabídku nikdy nepopsat jako garantovanou nebo bezpečnou.
2. **Vizuální důvěryhodnost:** odstranit CSS pseudoilustraci domu. Použít licencovanou architektonickou fotografii, anebo poctivě označený placeholder s art direction; fotografie není důkaz vlastnictví nemovitosti emitentem. Jeden vizuální jazyk, konzistentní typography/spacing, žádné typické AI gradienty a pestrobarevné generické karty.
3. **Kvalita leadu místo objemu e-mailů:** první jednoduché kvalifikační otázky, pak kontakt nutný pro zpřístupnění PDF (e-mail nebo telefon při nabídce konzultace); skutečné větvení pro >=50 000 Kč v blízké době, vzdálený termín, podlimitní a pouze informativní zájemce. Podlimitní lead nepovažovat za kvalifikovaného investora.
4. **Transparentní rizika:** nezaměňovat zajištění a garanci; dluhopis není pojištěný bankovní vklad. Uvést riziko ztráty jistiny a problematiku likvidity, zajištění a schopnosti emitenta splácet. Úrokovou sazbu, použije-li se, označit jako fiktivní předpoklad.
5. **Demo formulář:** neslibovat zaslání PDF, když neexistuje, a nepředstírat ukládání leadů. Veřejná ukázka nesmí návštěvníka zbytečně nutit zadat osobní kontaktní údaj. Je-li e-mailové pole zachováno, zjevně uvést, že není potřeba uvádět reálný e-mail a žádná data se neodesílají.
6. **Povinné odevzdání:** ověřená živá URL, veřejný GitHub repozitář, reálný export Claude Code `/export` ve složce `ai-log/`. Nefalšovat AI log, screenshoty ani výsledky testů.

## P1: kreativní a konverzní rozdíl

- Jediný konkrétní hero claim místo vágního sloganu; sekundární CTA „Jak dluhopis funguje“.
- Přehledný „ledger“ čtyř podmínek, srozumitelná časová osa a rozdělení mezi cashflow firmy a závazky vůči investorům.
- Lead magnet jako konkrétní rozhodovací pomůcka: „5 otázek před nákupem firemního dluhopisu“, s preview otázek a jednoduchým ilustračním výpočtem, ne prázdný „ebook zdarma“.
- FAQ reaguje na nejistoty začátečníka. Důvěru budují věcné podmínky, nikoli falešné reference, loga ČNB či fiktivní nemovitosti.
- Slib z reklamy se musí shodovat s hero, CTA a lead magnetem. CTA nemanipuluje časovým tlakem.
- Rozhodovací formulář má jasný úspěšný DEMO stav pro jednotlivé odpovědi a nejméně základní přístupnost (focus-visible, popisky, stavové hlášky, kontrast).

## Povinná reálná QA

1. Screenshoty a vizuální kontrola 375×812 a 1440×900; check i 320, 390, 768, 1024 px.
2. Ověř klikání všech CTA a navigace, formulář s >=50k, s <50k a pouze informativní odpovědí, invalidní e-mail a nulové odeslání dat.
3. Zkontroluj overflow, soulad s design reference lockem, velikost písma, ovládání klávesnicí, reduced motion, kontrast a alt.
4. Přečti všechny texty jako rodilý Čech. Zkontroluj jednotnou terminologii, vykání koncovému investorovi, žádné nesmyslné finance termíny.
5. Pokud nestíháš, nejdřív hero+mobil, funnel, transparentnost rizik a publikování. Animace poslední.
6. Napiš pravdivě, které testy jsi provedl a co zůstává neověřené.

## Interní hodnocení (0–5 za kategorii)

Originalita, vizuál, čitelnost 50+, vysvětlení finančního produktu a rizik, logika funnelu, copywriting, mobile UX, technické provedení, doložitelnost práce. Cíl alespoň 40/45, žádná oblast pod 4/5. Jde o vlastní heuristiku pro kontrolu, nikoli naměřené obchodní výsledky.

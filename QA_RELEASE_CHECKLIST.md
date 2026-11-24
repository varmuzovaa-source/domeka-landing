# DOMEKA — QA checklist (stav 24. 11. 2026)

Legenda: [x] ověřeno, [~] ověřeno částečně, [ ] neověřeno.

## Obsah / CRO
- [x] Hero na 375 px: produkt, minimum, splatnost, výplata, CTA v prvním viewportu (screenshot `mobile-375-first-screen.png`).
- [x] Primární CTA vede na průvodce, sekundární na „Jak dluhopis funguje“. Kotvy ověřeny v prohlížeči.
- [x] Lead magnet má konkrétní hodnotu (pět otázek, výpočet, otázky na poradce).
- [x] Telefon a e-mail jsou nepovinné. Zaškrtávací pole pro poradce se objeví jen u kvalifikovaného zájemce.
- [x] Pod minimem: vzdělávací výsledek, bez poradce.
- [x] Demo neslibuje odeslání ani PDF, nic neukládá. Skripty nevolají síť (jediný načtený zdroj je `hero-placeholder.svg`).
- [x] Žádné reference, certifikace ani schválení regulátora.
- [x] Fiktivní sazba označená na každém výskytu (hero, ledger, výpočet, FAQ, patička).
- [ ] Korektura češtiny rodilým mluvčím (provedena jen autorem).

## Frontend / přístupnost
- [x] Žádné horizontální přetečení: 320, 375, 390, 768, 1024, 1440 px (měřeno `scrollWidth`).
- [x] Screenshoty 320, 375, 390, 768, 1024, 1440 v `screenshots/`.
- [x] Větvení formuláře: 9 kombinací odpovědí, prázdné odeslání, špatný e-mail, špatný telefon, dokončení (automatizovaný test v prohlížeči).
- [x] Kontrasty spočítány (AA, viz `DESIGN_DECISIONS.md`).
- [x] Popisky polí, `fieldset/legend`, `role=alert`, focus se přesouvá na nadpis dalšího kroku.
- [~] Klávesnice a focus-visible: styl je v CSS a focus na nadpisech ověřen, ruční průchod celou stránkou klávesnicí neproběhl.
- [~] `prefers-reduced-motion`: plynulé rolování se zapíná jen bez omezení pohybu, jiné animace nejsou. Nezkoušeno s přepnutým systémovým nastavením.
- [ ] Čtečka obrazovky (VoiceOver) netestována.
- [ ] Safari/Firefox netestovány (testováno Chromium a headless Chrome). Používá se `:has()`, bez něj zůstává základní styl radií.
- [ ] Fotografie je placeholder, licencovaný snímek chybí.

## Odevzdání
- [ ] Veřejný GitHub repozitář.
- [ ] Vercel URL otevřená bez přihlášení.
- [ ] `ai-log/` s reálným exportem `/export` (nutné provést ručně).
- [ ] E-mail zadavateli připraven a schválen. Nic nebylo odesláno.

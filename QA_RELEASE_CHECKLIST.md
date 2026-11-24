# Domeka — ověření po jazykové, marketingové a technické revizi

Datum: 24. 11. 2026. Kontroloval Codex. Výchozí commit: 0f3fe8f; nové změny nejsou commitnuté ani nasazené.
SHA-256 kontrolovaného index.html: `4ecd4e27d58510c6e9c5ee83dd08b76763ba4e6294cbe85e96e39eb9991b571c`.

PASS = provedeno a prošlo; NOT-RUN = neprovedeno; N/A = mimo rozsah ukázky.

| Kontrola | Výsledek | Důkaz a rozsah |
|---|---|---|
| Čeština webu a PDF | PASS | Kompletní redakční revize, včetně popisků, chyb a čtyř výsledkových větví; nejde o nezávislou lidskou korekturu. |
| Výpočty | PASS | 50 000 × 0,072 = 3 600 ročně, 900 čtvrtletně, 14 400 za 4 roky; 150 mil. × 0,072 / 12 = 900 000; 900 000 / 14 000 zaokrouhleno na 65 celých bytů; u hrubého nájemného uvedena výhrada k nákladům a jistině. |
| Šířky a přetečení | PASS | Skutečně vykreslená stránka v rámcích šířky 320, 375, 390, 430, 639, 640, 759, 760, 767, 768, 859, 860, 979, 980, 991, 992, 1024, 1440 px. Ve všech scrollWidth = clientWidth. Výška průhledu 812 px. Jde o emulaci, nikoli fyzický telefon. |
| Minimální velikost textů | PASS | V uvedených šířkách nebyl ve zkoumaných viditelných textových prvcích nalezen text pod 16 px. Neplatí pro tiskové PDF. |
| Větvení formuláře | PASS | V běžném Chrome provedeno všech 20 kombinací 5 částek × 4 termíny. Konzultace jen od 50 000 a do 3 měsíců. |
| Kontakt jako podmínka PDF | PASS | Prázdný kontakt nelze dokončit. E-mail je výchozí, telefon po volbě konzultace je alternativou. Před kontaktem žádný viditelný odkaz na stažení. |
| Chybné vstupy | PASS | Běžný Chrome: prázdné odpovědi, chybný e-mail, chybějící telefon; text chyby a přesun fokusu. |
| Dokončení e-mailem | PASS | test@example.com → potvrzení bez předstírání doručení → zobrazen odkaz na PDF. |
| Dokončení telefonem | PASS | +420 777 123 456 → potvrzení bez předstírání hovoru → PDF. Opravena chyba normalizace předvolby +420. |
| Logika zdrojového skriptu | PASS | 41 kontrol v DOM simulaci: 20 větví, validace, vyčištění polí, hranice kalkulačky a přenos 50/100/500/1000 tisíc; simulace není vizuální test. |
| Kotvy a lokální soubory | PASS | 11 jedinečných lokálních odkazů/zdrojů; cíle existují. |
| PDF | PASS | Dvě strany, vizuálně prohlédnuté oba rendery; tabulka 50/100/250/500 tisíc odpovídá kalkulačce. |
| Přístupnost — zdroj | PASS | lang=cs, jedno h1, bez duplicitních id, label, fieldset/legend, chybové alerty, podmíněné required, aria-expanded, tmavý fokus v bílých kartách, skrytá lišta není fokusovatelná. |
| Omezený pohyb | PASS — zdroj | CSS vypíná animace a přechody; JS kontroluje prefers-reduced-motion u odezvy i posouvání. Přepnutí v nastavení OS nebylo testováno. |
| Kompletní klávesnice a VoiceOver | NOT-RUN | Přesun fokusu při validaci ověřen; kompletní ruční průchod klávesnicí ani čtečka nebyly provedeny. |
| Kompletní WCAG/axe | NOT-RUN | Neprohlašujeme úplnou shodu ani automatické skóre přístupnosti. |
| Lighthouse aktuální verze | NOT-RUN | Samostatný prohlížeč blokuje macOS MachPortRendezvous. Historické skóre 99/100/100/100 se nepřenáší na tuto revizi. |
| Safari, Firefox, fyzický mobil | NOT-RUN | Ověřeno běžné Chrome a vykreslení v rámcích, ne ostatní platformy. |
| Skutečné doručení a ukládání | N/A | Andrea výslovně zvolila ukázku pro zadání. Bez backendu, nikoli připravenost pro skutečnou kampaň. |
| Analytika | N/A | Pouze návrh měření, není nasazena a neposílá osobní údaje. |
| Doslovný Claude Code /export | NOT-RUN | Existující upravený přepis ponechán; nelze vydávat za přímý export. |
| Nové nasazení | NOT-RUN | Změny jsou pouze lokální; podle pravidel projektu commit/push až na výslovný pokyn. |

## Připravenost
Prototyp má opravenou cestu k získání kontaktu, poctivé stavy a nové PDF. Bez nového Lighthouse, úplné přístupnostní kontroly a ověření nasazení nelze poctivě potvrdit 9/10 ve všech technických disciplínách. Pro ostrou kampaň navíc chybí ověřené emisní podklady, skutečný emitent, právní posouzení, informace o zpracování údajů a funkční zpracování kontaktů.

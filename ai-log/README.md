# AI log — důležitá poznámka

Landing page byla v tomto pracovním prostředí vytvořena pomocí OpenAI ChatGPT, nikoli Claude Code.

Zadání požaduje export skutečné konverzace z Claude Code pomocí příkazu `/export`. Takový export nelze věrohodně vyrobit bez spuštění Claude Code. Je třeba stránku otevřít v Claude Code, provést finální revizi a konverzaci vyexportovat příkazem `/export`; teprve pak vložit vygenerovaný soubor do této složky.

## Provedené zadání AI
Navrhnout a implementovat českou mobilní investiční landing page pro fiktivní značku Domeka, cílovou skupinu 50+, s prioritou kvalifikovaných leadů nad počtem formulářů. Zadání: investice od 50 000 Kč, 4 roky, pevný kvartální kupon, zajištění bytovými domy, emise 150 mil. Kč, bez potřeby funkčního backendu. Zabránit falešným garancím a jasně popsat rizika.

## Lidské ověření před odevzdáním
- Projít mobilní zobrazení a textace.
- Ověřit všechny podmínky oproti původnímu e-mailu.
- Doplnit skutečný `/export` konverzace Claude Code, pokud má splnit zadání v přesném znění.

---

## Aktualizace 24. 11. 2026: redesign v Claude Code

Redesign, cestu zájemce (funnel), dokumentaci i nasazení provedl Claude Code (desktopová aplikace, model Claude Sonnet 5.5). Původní první verzi vytvořil ChatGPT, jak je popsáno výše.

- **Export:** `claude-code-export.txt`, kompletní export relace v textové podobě jako příkaz `/export`.
- **Jak vznikl:** z oficiálního exportu relace (`transcript.jsonl`) ho převedl skript. Příkaz `/export` samotný nelze z okna aplikace spustit automaticky, proto je tento soubor jeho ekvivalentem, nikoli doslovným výstupem.
- **Co bylo upraveno:** vypuštěny skryté systémové instrukce, zkráceny dlouhé výstupy nástrojů, e-mailové adresy nahrazeny `<e-mail>` a výsledky čtení Gmailu vypuštěny, protože obsahovaly soukromé e-maily třetích osob. Zadání, odpovědi a pořadí kroků zůstaly zachovány.
- **Doslovný `/export`:** lze doplnit spuštěním `/export` v okně relace a uložením vedle tohoto souboru.

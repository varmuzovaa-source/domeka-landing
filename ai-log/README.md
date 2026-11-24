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

Redesign, funnel, dokumentaci i nasazení provedl Claude Code (desktopová aplikace, model Claude Sonnet 5.5). Původní první verzi vytvořil ChatGPT, jak je popsáno výše.

- **Soubor:** `claude-code-session-2026-11-24.md`
- **Co to je:** čitelný přepis relace vygenerovaný skriptem z oficiálního exportu relace (`transcript.jsonl`). **Není to doslovný výstup příkazu `/export`**, protože slash příkaz lze spustit jen v interaktivním okně relace.
- **Co bylo upraveno:** vypuštěny skryté systémové instrukce, zkráceny dlouhé výstupy nástrojů, e-mailové adresy nahrazeny `<e-mail>` a výsledky čtení Gmailu vypuštěny, protože obsahovaly soukromé e-maily třetích osob. Text zadání, odpovědi a pořadí kroků zůstaly zachovány.
- **Doslovný `/export`:** pokud ho zadavatel vyžaduje přesně, lze ho doplnit spuštěním `/export` v této relaci a uložením vedle tohoto souboru.

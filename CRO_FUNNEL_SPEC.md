# Domeka — konverzní cesta a hypotézy

Aktuální návrh po závěrečné revizi. Předchozí varianty jsou dohledatelné v historii Git. Tento dokument popisuje návrh, nikoli naměřený obchodní výkon.

## Cíl

Získat kontakt na člověka s potenciálem investovat alespoň 50 000 Kč a připravit smysluplný rozhovor s poradcem. Deklarovaná částka a termín představují předběžnou kvalifikaci, nikoli ověření vhodnosti nebo potvrzenou investici.

## Cesta

1. Reklama přivede návštěvníka na nabídku se shodným sdělením. Skutečná reklamní kreativa není součástí odevzdání.
2. Úvod vysvětlí dluhopis, sazbu, minimum, splatnost a výplaty; na mobilu jsou podmínky a riziko před kalkulačkou.
3. Kalkulačka ukáže hrubé úroky a předá částku do formuláře.
4. Stránka vysvětlí podmínky, zdroj výplat a rizika.
5. Veřejný náhled představí hodnotu průvodce: pět kontrolních otázek, tabulku úroků a dotazy pro poradce.
6. Dvě otázky zjišťují částku a termín. Pásma částek se nepřekrývají.
7. Kontaktní krok vyžaduje e-mail. Zájemce od 50 000 Kč s termínem do tří měsíců může místo něj uvést telefon a požádat o konzultaci.
8. Po validaci se zpřístupní PDF. Ukázka údaje nikam neodesílá a neslibuje skutečné doručení nebo hovor.

## Větvení

- Od 50 000 Kč a do tří měsíců: průvodce a možnost konzultace.
- Od 50 000 Kč, později nebo nejistě: průvodce za e-mail, bez nabídky hovoru.
- Pod minimem: vzdělávací cesta za e-mail; bez nabídky hovoru a bez tlaku na zvýšení částky.
- Neurčená částka: informační cesta za e-mail, bez nabídky hovoru.

## Hypotézy k ověření

| Varianta | Co ověřovat |
|---|---|
| Úrok a výplata v úvodu oproti obnově domů | Přijaté kontakty a skutečné investice, společně s porozuměním rizikům. |
| Částka a termín před kontaktem oproti kontaktu na začátku | Podíl dosažitelných a poradcem přijatých kontaktů na 100 návštěv. |
| Název průvodce „Pět otázek před nákupem“ oproti „Dluhopis jednoduše“ | Přechod od vyžádání materiálu ke smysluplnému rozhovoru. |

## Měření pro ostrý provoz

Návštěva → otevření otázek → dokončení kvalifikace → skutečné doručení kontaktu → doručení nebo stažení průvodce → dosažitelný kontakt → poradcem přijatý zájemce → investice.

Úspěch kontaktu měřit až po potvrzení serverem, nikoli kliknutím. E-mailovou a telefonní cestu vyhodnocovat zvlášť. Do analytiky neposílat telefon ani e-mail. Klíčové ukazatele: podíl kvalifikovaných kontaktů, cena za kvalifikovaný kontakt, podíl skutečných investorů a cena za investora.

## Limity ukázky

Backend a měření nejsou podle zadání implementované. Kontakt se pouze validuje a následně zahodí. PDF není serverově chráněné, pouze není v rozhraní odkazované před kontaktem. Pro reálný provoz je nutné doplnit ukládání a doručování, datové podklady a právní posouzení. Žádný dopad na konverze nebyl naměřen.

> Current decision, 24 Nov 2026: Andrea wants a lead magnet exchanged for a contact. Show value first, ask amount and timing, then require an email or, for qualified consultation requests, a valid phone instead. No PDF link before this UI step. This remains a clearly labelled demo without data transmission. Older design examples below are historical and are superseded by this decision.

# DOMEKA — CRO funnel specification (handoff for Claude Code)

This supplements `CLAUDE_MASTER_PROMPT.md`. Do not treat hypotheses as measured findings.

## Single conversion objective
Qualified investor conversation, not a generic email capture. A marketing-qualified lead (MQL) is defined, for this fictional exercise, as a person who voluntarily expresses potential capacity **at least 50,000 CZK** and a willingness to learn the relevant terms and risks. A funded investor exists only after a verified investment, not after form submission.

### Promise continuity
Ad promise: `Jak může fungovat čtyřletý dluhopis financující obnovu bytových domů?` / landing hero: `Dluhopis na obnovu bytových domů. Nejprve porozumět. Potom se rozhodnout.` Avoid claims of safety, wealth protection, guaranteed income or superiority to savings.

Landing facts immediately readable:
- Minimální investice 50 000 Kč
- Splatnost 4 roky
- Pevný úrok; výplata čtvrtletně (rate only if explicitly invented, labeled and disclosed)
- Dluhopis nese riziko ztráty části nebo celé investice. Zajištění riziko neodstraňuje.

**Primary CTA:** `Prohlédnout podmínky a získat průvodce` (anchor to explanation/lead magnet; avoid claiming PDF already exists). **Secondary CTA:** `Jak dluhopis funguje`.

## Primary funnel — non-coercive and qualifying

**Step 0, no gate:** Learn 3 key terms and 2 material risks, an illustration of how payments *would* occur assuming the issuer performs. Clarify this is not an insured bank deposit. No fake property photos presented as issuer-owned.

**Step 1, lead-magnet proposition:** `5 otázek, které si položit před nákupem firemního dluhopisu`. Concrete preview: (1) komu půjčuji, (2) z čeho emitent splácí, (3) co je skutečně zastaveno a v jakém pořadí, (4) kdy mohu dostat peníze zpět, (5) co se stane při nesplácení. Explain what the user receives: short educational checklist, sample cashflow chart, call preparation questions. **The resource is now an actual two-page downloadable PDF, unlocked in the UI after a valid contact. The demo does not store or transmit data.**

**Step 2, two low-friction questions before email:**
Q1 `S jakou částkou přibližně počítáte?` values `Zatím zjišťuji` / `Méně než 50 000 Kč` / `50 000–99 999 Kč` / `100 000–499 999 Kč` / `500 000 Kč a více`. Avoid default selection.
Q2 `Kdy o investici případně uvažujete?` values `Jen sbírám informace` / `V příštích 3 měsících` / `Později` / `Nevím`.

**Step 3, proportional details:** Label `E-mail pro zaslání průvodce (ukázka)`; optional first name, optional phone with checkbox `Chci, aby se mi ozval poradce` (do not imply call automatically occurs, since demo has no backend). The form remains demo-only and shows a no-transmission confirmation such as `Ukázka dokončena. V této verzi se údaje nikam neodesílají a průvodce se automaticky neposílá.` Do not harvest real personal data in public demo; ideally avoid asking for a real full email at all or explicitly mark demo.

**Outcome branching:**
- Q1 >=50k + near-term intention: contact may be qualified for follow-up *subject to voluntary request and suitability checks*. No promises of approval or return.
- Q1 >=50k + research-stage: educational lead; do not prioritize with aggressive sales follow-up.
- Q1 <50k or unsure: educational lead only, **never** counted as funded-capable lead. Offer no-pressure explanation and exit.

### Form friction trade-off
Question-first flow filters at source but may lose some educational leads. Email-first grows total contacts but creates high advisor workload. Choose **light qualification before contact required to unlock the guide** because the client values funded investors, not CPL. Hypothesis only; validate with A/B tests.

## Page architecture and on-mobile priority
1. compact model disclaimer (sticky badge is optional if accessible)
2. readable company mark, one CTA
3. hero headline + one sentence + 50k / 4 yrs / quarterly facts + CTA, ideally within ~1 viewport at 375px; photo can follow the facts
4. building economics: acquisition -> renovation -> rent -> issuer obligations; avoid suggesting rental yield guarantees coupon payments
5. 3 terms in a well-ruled ledger, not fake traction metrics
6. plain-language risks and how security works / is unverified
7. lead-magnet value preview + qualifying 2-step form
8. skeptical FAQ, including bank deposit insurance and possible inability to sell early
9. finish with choice to read terms rather than pressure to sign

## Visual / copy QA
- On 375px: headline not cropped, CTA fully visible, numbers not wrapped awkwardly, mobile body >=16px, controls 44px+, form labels readable.
- Show the asset as a **conceptual architectural photo** or licensed relevant property, captioned `Ilustrační fotografie. Nejde o nemovitost společnosti Domeka.` Never fabricate real property collateral.
- Contrast WCAG AA; reduced motion; keyboard + focus-visible; no blocked scroll; no duplicate IDs.
- No bank/deposit comparison implying bond is as safe as a bank account.
- Never show approval, licensing, insurer icons or social proof unless grounded.

## A/B hypotheses for future real campaigns (not findings)
1. Hero focusing on `4 roky / kvartální výplata` vs `obnova bytových domů`: measure qualified-contact rate and funded-investor yield, with risk comprehension check.
2. Show 2 qualification questions before email vs after email: measure advisor-accepted leads per 100 ad clicks, not only raw email conversion.
3. Lead magnet `5 kontrolních otázek` vs `Dluhopis jednoduše`: measure download-to-meaningful-conversation rate and risk understanding, not clickbait opt-ins.

## Non-negotiable submission facts
- Fictional client and issuer; fictitious bond; no real investment offers or real leads.
- Target investment funding 150m CZK, principal and terms from the actual assignment.
- Confirm any invented coupon (e.g. 7.2% pa) is **explicitly invented and listed in README**; do not present 900 CZK quarter for 50k as guaranteed.
- GitHub public repo + deployed live site + genuine Claude Code `/export` are mandatory. Any missing must be reported, not disguised.

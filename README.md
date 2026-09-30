# INFERIVA — multi-page site

```bash
python3 build.py          # writes all 18 pages
python3 -m http.server 8000
```

Twenty-two pages, zero broken links, one shared shell.

**Aligned to the brand asset** — its taxonomy, its order, its register and its
visual weight.

**The site is organised around how you buy, not around what the product has.**
That was the rebuild: an earlier version was a product tour with good copy, and
a product tour is what every competitor already has.

---

## Why a generator rather than 18 hand-written files

The nav, footer, styles and contact form are defined once in `build.py`. Page
copy lives in `pages.py`. **The chrome cannot drift between pages**, and adding
a page is one entry rather than a copy-paste that slowly diverges.

Add a page: write the content in `pages.py`, add it to `NAV` in `build.py` if it
belongs in the menu, rebuild.

---

## The architecture, against the references

Youverify runs roughly thirty pages across Solution, Industry, Company,
Resources and Legal. **This is eighteen, deliberately.**

```
/                                  home — four ways in
/start/                            the commercial path
  diagnostic.html                  find out before you buy anything
  how-you-buy.html                 modules, metering, proration
/platform/                         overview
  onboarding.html                  the risk tier that survives to monitoring
  monitoring.html                  where the number came from
  cases.html                       the case opens with context already in it
  reporting.html                   filed, acknowledged, still explainable
  agent-networks.html              what a generic engine misses
/assurance/                        overview
  how-it-works.html                six steps, including the ones that cost time
  deliverables.html                four documents, four audiences
/sectors/                          who it's for
  payment-service-banks.html
  microfinance.html
  commercial-banks.html
  development-finance.html
/coverage.html                     markets, regulators, what binds vs informs
/company/about.html
/company/contact.html
```

**Every page has something specific to say.** A nav full of stubs is the first
thing that reads as a startup pretending to be a company, so the sections that
would need thin content — press, careers, glossary, blog, partners — are absent
until there is something to put in them.

---

## What each reference contributed

**MetaMap:** the clarity of a grid where each cell is a job the buyer
recognises, and pages that read as complete.

**Youverify:** the multi-level nav with dropdowns, product pages deep enough to
land on from search, and the sector pages. Their IA is the right shape for an
enterprise buyer who arrives via "transaction monitoring Nigeria" rather than
the homepage.

**Neither:** the logo strip, the metrics band, the customer stories. Three of
MetaMap's eleven homepage sections lean on commercial proof.

---

## Aligned to the brand asset

The asset was the better artefact and the site was not matching it. Four things
changed.

**Taxonomy.** AML · Fraud · Customer risk · Investigations · Regulatory
reporting · PSP and agent supervision. Two of those names are materially better
than what the site had: *"Customer risk"* is a business capability where
"Onboarding and KYC" is a process, and *"PSP and agent supervision"* frames a
network as something you oversee rather than a feature set. Fraud now has its
own page rather than living inside monitoring.

**Order — vision, then wedge.** The asset opens with *"One risk. One operating
platform"* and puts *"Start where the need is greatest"* near the end. The
earlier site led with the wedge and never stated the vision at all. **An
executive needs to see where this goes before they care that they can start
small.** That was backwards and is now fixed.

**Register.** The top of the site is now the board's: *"What changes for
leadership"*, *"Arrange an executive briefing"*, one connected view, governed
decisions, measurable improvement. The practitioner writing did not disappear —
it moved down into the module pages, where the person evaluating actually goes.
Both audiences are real and they read different pages.

**Visual weight.** The asset has photography, depth and iconography. The site had
austere type on white, which was a deliberate choice and indistinguishable from
unfinished. Added:

- **A connected-operations diagram**, drawn in SVG — six capabilities around one
  governed core. The argument made visually rather than asserted.
- **An icon set**, inline SVG, one per capability and one per leadership outcome.
- **Depth in the dark bands** — layered radial gradients and a faint masked grid,
  so the hero and the wedge band have the weight the asset has.
- **The strapline**, FINANCIAL CRIME. UNIFIED., closing the page as it closes
  the asset.

And the nav's call to action changed from *"Request a demo"* to *"Executive
briefing"*, which is the asset's own language and the right ask for the audience
the top of the site now addresses.

## What the earlier rebuild changed

**The proposition is now commercial, not functional.**

> You do not have to replace everything to fix something.

Most compliance platforms are sold as an estate — eighteen months, a steering
committee, a board paper. The code supports something quite different and the
site was not saying it:

- **A diagnostic** that needs an extract and nothing else — no integration, no
  procurement, no NDA
- **Modules entitled separately**, enforced in the platform rather than tracked
  in a spreadsheet
- **Four metering dimensions** counted independently, so an institution with
  high volume and few analysts is not priced like one with the opposite shape
- **Proration that splits the period** on a mid-month change

That last one is on the site because it is the kind of detail that tells a buyer
what sort of company they are dealing with: *"charging only the new plan
overcharges anyone who upgraded and undercharges anyone who downgraded."*

**Sophistication shows through the problems you have bothered to solve**, not
through a feature count. Nobody is impressed by 772 routes. Somebody who has
been mis-invoiced notices the proration paragraph.

## Where credibility comes from instead

Specificity, on every page. Real scenario names. Real provisions —
`POCAMLA s.44(6)`, `FIC Act s.42`, `MLR 2017 · SYSC 6.3`. A findings panel with
an actual finding and the obligations it puts at risk.

And candour used as a positioning device rather than a disclaimer:

> **About:** "We do not yet have SOC 2 Type II... We keep that list and we will
> show it to you — it is shorter than the one on the other side, and a vendor
> who cannot tell you what they have not done is a vendor who has not checked."

> **Coverage:** "Where a jurisdiction has not been reviewed by a qualified
> practitioner in that country, the report says so on the front page."

> **Assurance:** "It takes your senior compliance people's time. That is the
> point of it."

That reads as confidence rather than limitation, and it is the thing a
compliance buyer — who reads claims for a living — will actually respond to.

---

## Design

**Public Sans**, the US Web Design System typeface, drawn for government
communication. **IBM Plex Mono** for scenario codes and regulatory citations
only, because those are identifiers.

Your `#12355b` and `#0f5fb8`. The `#2ac7bf` teal is deliberately absent — it
sits close to Youverify's `#277A93`.

Rules rather than shadows, square rather than rounded. Both references use soft
cards; this reads as a document, which suits the subject and distinguishes it at
a glance.

---

## Before publishing

**One line, in `build.py`:**

```python
<form id="enquiry" action="https://formspree.io/f/REPLACE_ME" ...>
```

Until you change it the form says *"Form endpoint not configured"* rather than
pretending to send. The form appears on every page, so this is one change for all
eighteen.

**Then, as they arrive:** SOC 2 in the footer, a named production reference, and
real figures in the findings panel. Each makes the site stronger. **None is
needed for it to be credible.**

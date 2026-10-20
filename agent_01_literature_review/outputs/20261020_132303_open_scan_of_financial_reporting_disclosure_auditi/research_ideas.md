# Research Idea Bank
_Run 2026-10-20 13:23 · topic: Open scan of financial reporting, disclosure, auditing, and tax opportunities; news window April 20–October 20, 2026; literature window 2000–2026._

**5 new · 0 updated · 10 ideas in bank · 30 papers reviewed in total**

## Overview

| ID | This run | Idea | Novelty | Data | Last updated |
|---|---|---|---|---|---|
| I-006 | 🆕 new | [1. What Is Inside Reported Cash? Cash-Equivalent Composition and the Credibility of Corporate Liquidity](#i-006) | 4/5 | high | 2026-10-20 13:23 |
| I-007 | 🆕 new | [2. Paying the Customer's Customer: Revenue Deductions, Operating Expenses, and Top-Line Comparability](#i-007) | 4/5 | medium | 2026-10-20 13:23 |
| I-008 | 🆕 new | [3. Cyber Materiality Labels versus Realized Accounting Losses](#i-008) | 2/5 | medium | 2026-10-20 13:23 |
| I-009 | 🆕 new | [4. From Carbon-Intensity Evidence to Recognized Tax Credits: Section 45Z Verification and Earnings](#i-009) | 4/5 | medium | 2026-10-20 13:23 |
| I-010 | 🆕 new | [5. Mortgage-Servicing Recapture: Better Fair Values or More Unverifiable Optimism?](#i-010) | 4/5 | medium | 2026-10-20 13:23 |
| I-001 | — | [1. From Tariff Refund Claims to Reported Earnings: Recognition, Classification, and Auditor Coordination](#i-001) | 4/5 | medium | 2026-10-20 09:09 |
| I-002 | — | [2. The Unexplained Remainder: Residual Aggregation under the New Income Tax Disclosures](#i-002) | 2/5 | medium | 2026-10-20 09:09 |
| I-003 | — | [3. Quality-Control Compliance Costs and Small-Auditor Client Retention](#i-003) | 4/5 | low | 2026-10-20 09:09 |
| I-004 | — | [4. Climate Disclosure Retrenchment or Relocation into Financial Reporting?](#i-004) | 2/5 | medium | 2026-10-20 09:09 |
| I-005 | — | [5. Voluntary Quarterly Disclosure as a Commitment When Mandatory Frequency Is Uncertain](#i-005) | 2/5 | low | 2026-10-20 09:09 |

## New and updated ideas this run

---

<a id="i-006"></a>
### I-006 · 1. What Is Inside Reported Cash? Cash-Equivalent Composition and the Credibility of Corporate Liquidity (🆕 new)
**Novelty** ★★★★☆ · **Data feasibility** `high` · first seen 2026-10-20 13:23 · last updated 2026-10-20 13:23

> **Research question.** Does separately identifying the composition of cash equivalents improve the informativeness of reported corporate liquidity, and does investors' valuation of cash depend on that composition?

| | |
|---|---|
| **What it is** | Construct a reconciliation of reported cash and cash equivalents to separately quantified instrument classes, distinguishing bank deposits, money-market funds, government securities, other instruments, and an unexplained remainder. Test whether composition and reconciliation completeness explain investors' assessments of liquidity beyond the headline balance. The August 2026 taxonomy proposal motivates an immediately feasible baseline study and a prospective regulatory follow-up, not an already-implemented mandatory-disclosure experiment. FASB's project separately addresses significant classes of cash equivalents and digital-asset classification. ([fasb.org](https://fasb.org/projects/fasb-taxonomies/taxonomy-updates-and-news?utm_source=openai)) |
| **Gap** | 10.1016/j.jacceco.2011.07.001 links general transparency to trading-liquidity uncertainty, while 10.1111/j.1475-679x.2007.00238.x explains information-quality effects on assessed risk. Neither directly evaluates a reconciliation of corporate cash-equivalent instrument classes. 10.2139/ssrn.7470320 studies reserve disclosures by stablecoin issuers, not the liquidity reporting of corporate holders. |
| **Novel angle** | A dollar-based, auditable composition measure rather than a generic liquidity-disclosure score. Digital assets are an optional subgroup, not an assumed large treated sample. |
| **Accounting angle** | The question concerns balance-sheet classification, footnote disaggregation, reconciliation completeness, and the decision-usefulness of a prominent accounting aggregate. |
| **Identification** | Begin with a 2018–2026 firm-year panel and within-firm changes in quantified composition disclosure. Use firm and year effects, matched observations, and controls for actual portfolio changes; describe these estimates as associations because disclosure choice is endogenous. Preregister a conditional future difference-in-differences design comparing firms with large versus small pre-rule disclosure gaps only if a final rule, effective date, and usable post-adoption observations emerge. Do not treat an August taxonomy proposal as an adoption mandate. |
| **Risks** | Voluntary disclosure is endogenous; instrument classes can overlap across footnotes; cash-equivalent totals are sometimes not separately observable. Ballis et al.'s stablecoin-reserve paper and the FARS paper Corporate Crypto Holdings and Analysts' Forecasting Environment create adjacent overlap. Conference screening was partial, so this is not a novelty clearance. |

**Hypotheses**
- H1: More complete instrument-class reconciliation is associated with less uncertainty around liquidity-related disclosures, conditional on cash balances and firm fundamentals.
- H2: The association between reported cash and equity value varies with disclosed instrument composition and accessibility.
- H3: Incremental disaggregation is more informative when the previously unexplained cash-equivalent remainder is larger.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, I/B/E/S, Audit Analytics
- **Disclosure text:** SEC EDGAR 10-K cash, investments, fair-value, and significant-accounting-policy footnotes, SEC EDGAR 10-Q updates, SEC EDGAR comment letters concerning cash-equivalent classification
- **Sample:** US domestic public companies with usable 10-K filings, 2018–October 20, 2026. Start with a stratified manual validation sample before full extraction; exclude financial firms from the primary specification and analyze them separately.
- **Key variables:**
  - Composition completeness: separately quantified cash-equivalent classes divided by the disclosed cash-equivalent total; construct only when the denominator and mutually exclusive classes are observable.
  - Unexplained remainder: disclosed cash-equivalent total less identifiable instrument-class amounts; retain measurement-quality flags.
  - Composition shares: instrument-class amounts divided by the cash-equivalent total; do not infer undisclosed deposits or assume an unexplained remainder is risky.
  - Outcomes: filing-window absolute abnormal returns, subsequent return volatility, analyst forecast dispersion, and market-value associations with cash balances.
  - Controls: size, leverage, profitability, cash holdings, investment intensity, industry-year conditions, and observable changes in instrument composition.
- **EDGAR check:** Query: "cash equivalents" "money market"; forms: 10-K; January 1, 2024–October 20, 2026. Returned 10,000 hits, explicitly a lower-bound/capped result; 98 unique filings in the returned sample. This establishes text availability, not the number of firms with extractable instrument amounts.
- **Feasibility notes:** All proposed WRDS subscriptions are marked assumed, not confirmed. Free EDGAR supports the core extraction. Cash, cash equivalents, and short-term investments must not be conflated. The current causal-regulation extension is prospective; machine-readable taxonomy changes may mechanically improve tagging without changing economic disclosure.

</details>

<details><summary><b>News triggers</b></summary>

- [XBRL Staff Issues Proposed GAAP Taxonomy Improvements for Proposed Update on Enhanced Disclosures of Cash Equivalents](https://fasb.org/projects/fasb-taxonomies/taxonomy-updates-and-news) — FASB, 2026-08-25

</details>

<details><summary><b>Related papers</b></summary>

- Transparency and liquidity uncertainty in crisis periods (Mark Lang, Mark Maffett, 2011, Journal of Accounting and Economics)
- Accounting Information, Disclosure, and the Cost of Capital (Richard A. Lambert, Christian Leuz, Robert E. Verrecchia, 2007, Journal of Accounting Research)
- When Is Private Money Information-Sensitive? Evidence from Stablecoin Reserve Disclosures (Antonis Ballis, Phuong Anh Nguyen, Dimitrios Anastasiou, 2026, SSRN; Swiss Finance Institute Research Paper Series 26-64)
- Corporate Crypto Holdings and Analysts’ Forecasting Environment (Yi Huang, Adriana Korczak, Nikolaos Tsileponis, 2026, 2026 FARS Midyear Meeting)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 13:23 — 20261020_132303_open_scan_of_financial_reporting_disclosure_auditi

</details>

---

<a id="i-007"></a>
### I-007 · 2. Paying the Customer's Customer: Revenue Deductions, Operating Expenses, and Top-Line Comparability (🆕 new)
**Novelty** ★★★★☆ · **Data feasibility** `medium` · first seen 2026-10-20 13:23 · last updated 2026-10-20 13:23

> **Research question.** Does discretion over payments beyond the immediate customer relationship impair revenue comparability even when operating income and cash flows are unchanged?

| | |
|---|---|
| **What it is** | Identify arrangements in which an issuer pays on behalf of its customer or pays its customer's customer, then hand-code whether the payment reduces revenue or enters operating expenses. Test whether economically similar arrangements generate different reported revenue growth and margins, and whether explicit contractual promises explain classification. FASB's August 19, 2026 decisions identify this precise boundary issue; they are tentative decisions rather than current changes to GAAP. ([fasb.org](https://fasb.org/projects/current-projects/consideration-payable-to-a-customer-425308?utm_source=openai)) |
| **Gap** | 10.2308/tar-2022-0298 studies principal-versus-agent assessments and compliance risk. 10.1111/1911-3846.12775 studies discretion over the timing of multiple-deliverable revenue. These papers do not directly test classification of payments to a customer's customer or payments made on a customer's behalf. |
| **Novel angle** | Focuses on the identity of the ultimate payment recipient and the contractual promise linking the payment to a sale. Separates presentation-only effects from changes in underlying activity. |
| **Accounting angle** | This is a revenue-measurement and presentation question involving the boundary between consideration payable to a customer and a separately purchased service. |
| **Identification** | First estimate matched-arrangement comparisons within narrow business models, controlling for payment purpose and contractual substance. Reconstruct presentation-neutral revenue and expense measures only where disclosed amounts permit it. Treat current results as descriptive or associational. If guidance is finalized, use pre-announcement contractual exposure and classification practice to define treatment intensity in a future event-study/DiD design; early adoption would require explicit selection analysis. |
| **Risks** | The directly exposed sample could be much smaller than the EDGAR hit count. Contractual differences may justify different accounting, so classification dispersion alone is not evidence of manipulation. Du et al. provide a close methodological precedent. Distinguish this project from the separate 2025 share-based-consideration standard. |

**Hypotheses**
- H1: Similar indirect-customer payment arrangements exhibit economically meaningful variation between revenue deductions and operating-expense presentation.
- H2: Classification differences explain reported revenue-growth and margin differences more strongly than operating-income or cash-flow differences.
- H3: More explicit contractual promises are associated with less classification dispersion and fewer classification-related SEC inquiries.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, I/B/E/S, Audit Analytics
- **Disclosure text:** SEC EDGAR revenue-recognition and customer-incentive footnotes, SEC EDGAR 10-K and 10-Q discussion of rebates, incentives, and indirect-customer payments, SEC EDGAR exhibits containing relevant commercial agreements, SEC EDGAR revenue-classification comment letters
- **Sample:** US issuers with relevant arrangements, 2018–October 20, 2026; subsequent adoption analysis conditional on final guidance. Begin with platforms, intermediaries, and distribution-intensive businesses, but determine inclusion from contracts rather than industry labels.
- **Key variables:**
  - Exposure: pre-August 19, 2026 disclosure of payments to a customer's customer or payments made on a customer's behalf, manually distinguished from ordinary direct rebates.
  - Classification: reduction of revenue, operating expense, mixed treatment, or indeterminate.
  - Contract linkage: explicit promise, disclosed implicit expectation, separately identifiable service, and ultimate recipient.
  - Presentation-neutral measures: reconstructed revenue growth and expense ratios only for observations with quantified payments and an unambiguous accounting bridge.
  - Outcomes: revenue forecast errors, cross-firm margin dispersion, relevant comment letters, audit fees, and classification-related CAMs.
  - Controls: size, profitability, sales growth, acquisitions, business model, and direct-customer incentive exposure.
- **EDGAR check:** Query: "consideration payable" "customer"; forms: 10-K,10-Q; January 1, 2024–October 20, 2026. Returned 4,495 hits; 99 unique filings in the returned sample. Hits are broad screening evidence and do not establish the size of the indirect-customer subgroup.
- **Feasibility notes:** WRDS access is assumed. The critical subgroup requires substantial manual screening; many phrase hits concern direct-customer payments or unrelated uses of consideration. Quantified payment amounts may be unavailable. No final standard or mandatory treatment date is assumed.

</details>

<details><summary><b>News triggers</b></summary>

- [FASB adds Consideration Payable to a Customer project and completes initial deliberations](https://fasb.org/projects/current-projects/consideration-payable-to-a-customer-425308) — FASB, 2026-08-19

</details>

<details><summary><b>Related papers</b></summary>

- Principal-versus-Agent Considerations in Revenue Recognition Under ASC 606 and Compliance Risk (Kai Du, Henock Louis, Brent A. Schmidt, 2026, The Accounting Review)
- The Impact of Managerial Discretion in Revenue Recognition: A Reexamination (Linda A. Myers, Roy Schmardebeck, Timothy A. Seidel, 2022, Contemporary Accounting Research)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 13:23 — 20261020_132303_open_scan_of_financial_reporting_disclosure_auditi

</details>

---

<a id="i-008"></a>
### I-008 · 3. Cyber Materiality Labels versus Realized Accounting Losses (🆕 new)
**Novelty** ★★☆☆☆ · **Data feasibility** `medium` · first seen 2026-10-20 13:23 · last updated 2026-10-20 13:23

> **Research question.** How informative are initial cyber-incident materiality assessments about subsequent financial-statement consequences, and when do assessment-to-outcome discrepancies lead to auditor or control-reporting responses?

| | |
|---|---|
| **What it is** | Follow disclosed cybersecurity incidents from their initial 8-K item and materiality language through subsequent recognized expenses, insurance recoveries, operational disruptions, and control disclosures. Evaluate whether an initially nonmaterial or unresolved assessment predicts later accounting consequences and whether auditor reporting changes when the assessment and realized consequences diverge. The October 2, 2026 industry letter motivates the policy question but is advocacy, not evidence that disclosure requirements were repealed. ([sec.gov](https://www.sec.gov/comments/CLL-15/cll15-1082159-3759646.pdf?utm_source=openai)) |
| **Gap** | 10.1287/mnsc.2023.01058 documents potential manipulation of incident discovery dates. 10.2139/ssrn.7397253 examines annual Item 1C governance and materiality disclosures. The conference paper Shifts in Cybersecurity Breach Disclosure Following SEC Item 1.05 overlaps directly with filing-channel choice. The proposed contribution therefore excludes a standalone study of channel substitution and instead examines the incident-to-recognition-to-audit sequence. |
| **Novel angle** | A validated incident-level accounting ledger that separates gross costs, insurance recoveries, recognized versus estimated amounts, and revisions to prior assessments. A subsequent loss is not automatically coded as evidence that an earlier assessment was wrong. |
| **Accounting angle** | Connects event disclosure to recognized losses, recoveries, estimates, disclosure controls, internal control over financial reporting, and audit reporting. |
| **Identification** | Use incident-level predictive validation and within-issuer comparisons where repeated incidents exist. Define assessment revisions separately from realizations caused by genuinely new information. Estimate matched incident panels using initial disclosed severity, operating disruption, and firm characteristics. Do not interpret filing under Item 8.01 versus Item 1.05 as randomly assigned, and do not use the CTIA letter as an exogenous regulatory shock. |
| **Risks** | High scoop risk: Badger, Binkley, and Arthur's conference paper already studies shifts following Item 1.05; its full manuscript was not obtained. Badger et al.'s Item 1C working paper is also close. Selection into disclosure, incomplete loss measurement, hindsight bias, and a small number of audit-reporting changes are major threats. Obtain both manuscripts before committing. |

**Hypotheses**
- H1: Initial materiality language predicts subsequent quantified financial consequences, but predictive accuracy varies with estimation uncertainty.
- H2: Weak disclosure controls are associated with larger subsequent revisions to initially disclosed financial-impact estimates.
- H3: Unexpectedly large subsequent consequences are associated with additional control reporting or audit attention, conditional on incident severity.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, Audit Analytics
- **Disclosure text:** SEC EDGAR 8-K Items 1.05, 8.01, and 7.01 and amendments, SEC EDGAR 10-K Item 1C, Item 9A, loss-contingency and insurance footnotes, SEC EDGAR 10-Q incident-cost updates and auditor-report CAMs
- **Sample:** Incidents disclosed by US domestic issuers from December 18, 2023 through October 20, 2026. Primary realization tests require a fixed follow-up horizon; recent incidents enter only descriptive analyses until sufficient follow-up exists.
- **Key variables:**
  - Initial assessment: material, not material, unresolved, or no explicit assessment; record the filing item separately.
  - Accounting consequences: incident-specific recognized expense, impairment, liability, and insurance recovery amounts; avoid summing repeated cumulative disclosures.
  - Revision: changes to explicit prior financial-impact estimates, with a separate new-information flag.
  - Audit/control outcomes: cyber- or IT-related material weaknesses, audit-report lag, audit fees, and incident-related CAM language.
  - Prediction outcomes: out-of-sample classification and amount-prediction performance, evaluated against subsequent disclosed consequences rather than an unobservable complete-loss measure.
  - Controls: initial operating disruption, size, industry, prior incidents, profitability, leverage, and pre-existing control weaknesses.
- **EDGAR check:** Query: "cybersecurity incident"; forms: 8-K; December 18, 2023–October 20, 2026. Returned 1,177 hits; 91 unique filings in the returned sample. Amendments, exhibits, and repeated incident updates require deduplication.
- **Feasibility notes:** WRDS access is assumed. EDGAR supplies a feasible incident universe, but quantified costs and recoveries are selectively disclosed. Do not code nondisclosure as zero loss. Public filings cannot identify all undisclosed incidents, and October 2026 incidents are right-censored.

</details>

<details><summary><b>News triggers</b></summary>

- [CTIA requests reform of cybersecurity disclosures in comment on Reforming Regulation S-K](https://www.sec.gov/comments/CLL-15/cll15-1082159-3759646.pdf) — CTIA comment letter filed with the SEC, 2026-10-02

</details>

<details><summary><b>Related papers</b></summary>

- Timely Cybersecurity Disclosure and Information Manipulation (Xuanpu Lin, Guoman She, 2025, Management Science)
- Fortifying the Nonbreached: Auditors’ Role in Cybersecurity Risk Management (Xiaomeng Charlene Chen, Jengfang Chen, Rongrong Chen, 2025, Auditing: A Journal of Practice & Theory)
- Cybersecurity Risk Governance and Materiality Assessments in Item 1C Disclosures (Jack Badger, Marcy Binkley, Deanie Chaudoin, 2026, SSRN)
- Shifts in Cybersecurity Breach Disclosure Following SEC Item 1.05 (Jack Badger, Marcy Binkley, Jacob Arthur, 2026, 2026 AAA AIS/SET Meeting)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 13:23 — 20261020_132303_open_scan_of_financial_reporting_disclosure_auditi

</details>

---

<a id="i-009"></a>
### I-009 · 4. From Carbon-Intensity Evidence to Recognized Tax Credits: Section 45Z Verification and Earnings (🆕 new)
**Novelty** ★★★★☆ · **Data feasibility** `medium` · first seen 2026-10-20 13:23 · last updated 2026-10-20 13:23

> **Research question.** Does verifiability of emissions inputs constrain recognition of clean-fuel credits, and does stronger substantiation reduce subsequent accounting revisions?

| | |
|---|---|
| **What it is** | Study whether the availability of substantiating emissions evidence affects the timing, estimation, and presentation of Section 45Z benefits. Build a project-to-disclosure ledger recording credit estimates, recognized benefits, receivables, transfers, and subsequent revisions. Notice 2026-53 supplies a concrete verification setting through emissions-rate guidance, agricultural-practice provisions, and manure-specific substantiation requirements; it does not establish a universal recognition date for financial reporting. ([irs.gov](https://www.irs.gov/newsroom/irs-issues-notice-on-45z-clean-fuel-production-tax-credit-to-support-domestic-biofuel-production-and-american-agriculture?trk=article-ssr-frontend-pulse_little-text-block&utm_source=openai)) |
| **Gap** | 10.1007/s11142-025-09914-3 shows that narrative disclosures predict tax outcomes. 10.1007/s11142-025-09884-6 studies consequences of tax KAMs for tax-attribute valuation and auditor-provided tax services. Neither directly traces how technical emissions substantiation translates into recognition and realization of transferable clean-fuel benefits. |
| **Novel angle** | Links engineering-verification disclosures to accounting recognition milestones. Classify each issuer's stated accounting policy before choosing outcomes; do not presume every 45Z benefit appears in income-tax expense. |
| **Accounting angle** | Examines financial reporting for tax-related government benefits, accounting-policy choice, estimation uncertainty, recoverability, and auditability—not simply whether tax incentives increase investment. |
| **Identification** | Use the September 8, 2026 notice as an information milestone, interacted with project pathways and unresolved-methodology exposure identified from pre-notice filings. Compare affected and less-affected pathways within issuers where possible. Because pathway selection and eligibility economics are endogenous, present initial estimates as differential information responses rather than clean causal accounting effects. Separate changes in credit entitlement from changes in measurement certainty; use exact inference or descriptive comparative cases if the issuer count is small. |
| **Risks** | Small treated sample, selective project disclosure, simultaneous changes in entitlement and verifiability, and heterogeneous accounting policies. The specific agronomic substantiation needed for a strong mechanism test may be absent from public filings. Broad SSRN results were weakly relevant, so novelty remains provisional. |

**Hypotheses**
- H1: Issuers disclosing stronger substantiation of relevant emissions inputs recognize less uncertain credit amounts and subsequently revise them less.
- H2: Guidance resolution is associated with larger recognition updates for projects whose previously disclosed estimates depended on unresolved methodologies.
- H3: More complete recognition-to-transfer reconciliations improve the predictability of subsequent reported cash realization.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, Audit Analytics
- **Disclosure text:** SEC EDGAR 10-K and 10-Q disclosures mentioning Section 45Z, SEC EDGAR income-tax, government-assistance, receivable, and accounting-policy footnotes, SEC EDGAR 8-K earnings releases and disclosed credit-transfer agreements
- **Sample:** US public issuers disclosing actual or expected Section 45Z exposure, 2024–October 20, 2026; follow-up recognition and realization tests require later filings. Count distinct issuers and projects before selecting an archival versus comparative-case design.
- **Key variables:**
  - Predetermined exposure: disclosed project feedstock/pathway and dependence on unresolved emissions methodologies before September 8, 2026.
  - Substantiation: explicit discussion of certification, lifecycle-model inputs, agricultural-practice evidence, or farm-specific records; distinguish evidence possession from generic compliance language.
  - Recognition ledger: benefit recognized, statement location, credit receivable, amounts transferred, cash collected, and valuation adjustments, only where separately disclosed.
  - Revisions: changes in estimated credit amounts with disclosed reasons; separate policy changes, production changes, price changes, and methodology updates.
  - Controls: production or project scale where disclosed, profitability, leverage, liquidity, and other energy-credit exposure.
- **EDGAR check:** Query: "45Z"; forms: 10-K,10-Q; January 1, 2024–October 20, 2026. Returned 152 hits; 93 unique filings in the returned sample. These are filings, not 93 firms; sample hits include repeated issuers and exhibits.
- **Feasibility notes:** WRDS access is assumed. The number of independently treated issuers may be small, and pathway-level amounts may not be disclosed. Third-quarter 2026 reporting is largely not yet available at the cutoff. Do not promise a completed post-notice panel or infer private transfer prices.

</details>

<details><summary><b>News triggers</b></summary>

- [IRS issues notice on 45Z Clean Fuel Production Tax Credit to support domestic biofuel production and American agriculture](https://www.irs.gov/newsroom/irs-issues-notice-on-45z-clean-fuel-production-tax-credit-to-support-domestic-biofuel-production-and-american-agriculture) — IRS, 2026-09-08

</details>

<details><summary><b>Related papers</b></summary>

- Using narrative disclosures to predict tax outcomes (Olga Bogachek, Antonio De Vito, Paul Demeré, 2025, Review of Accounting Studies; online publication 2025, volume 31 in 2026)
- The consequences of expanded audit reporting: implications of tax key audit matters for tax attribute valuation and auditor-provided tax services (Daniel P. Lynch, Aaron J. Mandell, Linette M. Rousseau, 2025, Review of Accounting Studies)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 13:23 — 20261020_132303_open_scan_of_financial_reporting_disclosure_auditi

</details>

---

<a id="i-010"></a>
### I-010 · 5. Mortgage-Servicing Recapture: Better Fair Values or More Unverifiable Optimism? (🆕 new)
**Novelty** ★★★★☆ · **Data feasibility** `medium` · first seen 2026-10-20 13:23 · last updated 2026-10-20 13:23

> **Research question.** When does including expected recapture improve the predictive validity of mortgage-servicing-right fair values, and when does it mainly expand managerial discretion?

| | |
|---|---|
| **What it is** | Compare mortgage-servicing-right valuations across issuers that explicitly include recapture, explicitly exclude it, or do not explain their practice. Examine whether disclosed recapture assumptions predict subsequent servicing retention and fee income, and whether they improve valuation comparability or introduce optimistic discretion. The September 23, 2026 proposal would include recapture in measurement, but a mandatory-adoption study is not yet available. ([journalofaccountancy.com](https://www.journalofaccountancy.com/news/2026/sep/fasb-proposes-update-to-residential-mortgage-servicing-rights-guidance/?utm_source=openai)) |
| **Gap** | 10.1007/s11142-013-9234-y directly compares managerial and market inputs in MSR valuations. 10.1007/s11142-026-09949-0 examines incentives behind sticky Level 3 valuations in mutual funds. Neither specifically tests recapture inclusion and the measurement-versus-disclosure trade-off in the 2026 MSR proposal. |
| **Novel angle** | An assumption-level validation of recapture, not a generic Level 3 valuation study. Distinguishes existing economic recapture capability from the accounting decision to include its value. |
| **Accounting angle** | A fair-value measurement, unit-of-account, estimation-disclosure, and auditing question concerning an identifiable Level 3 asset. |
| **Identification** | Start with a longitudinal descriptive/predictive design using pre-proposal policy classifications and within-issuer assumption changes. Hold out future observations for validation and control for contemporaneously disclosed prepayment, discount-rate, and portfolio changes. A future adoption design would interact pre-rule exclusion practices with final implementation, but would require sufficient independent issuers and controls for refinancing conditions. Do not impose a treatment date or effective date absent final guidance. |
| **Risks** | A small, concentrated sample; changing refinancing economics; acquisitions; and limited observation of recapture assumptions threaten identification. Altamuro and Zhang is a very close asset-setting precedent. Much existing practice may already incorporate recapture, leaving little measurement treatment. |

**Hypotheses**
- H1: Explicitly disclosed recapture assumptions improve prediction of subsequent retained servicing and servicing-fee income when supported by observable historical performance.
- H2: Unsupported recapture assumptions are associated with more subsequent downward valuation revisions.
- H3: Harmonized measurement improves comparability less when recapture assumptions remain undisclosed.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, Audit Analytics
- **Disclosure text:** SEC EDGAR MSR fair-value, impairment, and sensitivity footnotes, SEC EDGAR servicing-portfolio and refinancing-retention disclosures, SEC EDGAR auditor reports and MSR-related CAMs, SEC EDGAR transition disclosures if final guidance is adopted later
- **Sample:** US listed banks, mortgage companies, and mortgage REITs with material residential MSRs, 2018–October 20, 2026. Analyze entity types separately and first establish the number of independent issuers with observable accounting-policy variation.
- **Key variables:**
  - Recapture policy: explicitly included, explicitly excluded, implicit/unclear, or not discussed; do not equate no discussion with exclusion.
  - Valuation: MSR carrying value and fair value relative to unpaid principal balance or servicing fees, where available.
  - Assumptions: recapture rates, prepayment speeds, discount rates, servicing costs, and sensitivity disclosures.
  - Validation outcomes: subsequent disclosed retained servicing, recapture activity, servicing fees, impairment, and valuation revisions.
  - Audit outcomes: MSR CAM specificity, audit fees, and valuation-related control disclosures.
  - Controls: portfolio size and composition, disclosed refinancing conditions, hedging results, and servicing acquisitions or sales.
- **EDGAR check:** Query: "mortgage servicing rights" "recapture"; forms: 10-K,10-Q; January 1, 2024–October 20, 2026. Returned 520 hits; 98 unique filings in the returned sample. Repeated PennyMac and other servicer filings indicate concentration, not 98 independent firms.
- **Feasibility notes:** WRDS access is assumed. Free filings contain relevant disclosures, but the independently treated issuer count and explicit recapture assumptions may be limited. The proposal does not establish an effective date. No new recurring recapture-specific disclosure is assumed.

</details>

<details><summary><b>News triggers</b></summary>

- [FASB proposes update to residential mortgage servicing rights guidance](https://www.journalofaccountancy.com/news/2026/sep/fasb-proposes-update-to-residential-mortgage-servicing-rights-guidance/) — Journal of Accountancy, 2026-09-23
- [XBRL Staff Issues Proposed GAAP Taxonomy Improvements for Proposed Update on Mortgage Servicing Rights - Recapture](https://fasb.org/projects/fasb-taxonomies/taxonomy-updates-and-news) — FASB, 2026-09-23

</details>

<details><summary><b>Related papers</b></summary>

- The financial reporting of fair value based on managerial inputs versus market inputs: evidence from mortgage servicing rights (Jennifer Altamuro, Haiwen Zhang, 2013, Review of Accounting Studies)
- Why are reported fair values sticky? (Paul Fischer, David Haushalter, Brian Miller, 2026, Review of Accounting Studies)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 13:23 — 20261020_132303_open_scan_of_financial_reporting_disclosure_auditi

</details>

## Earlier ideas

<a id="i-001"></a>
<details><summary><b>I-001 · 1. From Tariff Refund Claims to Reported Earnings: Recognition, Classification, and Auditor Coordination</b></summary>

**Novelty** ★★★★☆ · **Data feasibility** `medium` · first seen 2026-10-20 09:09 · last updated 2026-10-20 09:09

> **Research question.** How do verification milestones and auditor coordination affect the timing and income-statement classification of tariff refund recognition?

| | |
|---|---|
| **What it is** | Construct a firm-quarter panel tracking the first disclosure, recognition, classification, and subsequent collection of IEEPA tariff refunds. CBP's April 20, 2026 CAPE launch and May 4 explanation of claim-monitoring reports provide observable administrative milestones, but not automatically exogenous firm-level claim approval dates. Study whether firms facing similar disclosed refund uncertainty report different earnings effects and whether reporting choices converge within auditor portfolios. The CBP bulletin confirms that principal, interest, and processing status can be separately tracked by claimants. ([content.govdelivery.com](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/415c8e9?reqfrom=share)) |
| **Gap** | 10.1111/1475-679x.12053 studies preparer judgments for contingent liabilities, rather than recoveries. 10.1016/j.jacceco.2014.08.007 models asymmetric disclosure rules. Neither retrieved abstract addresses administrative verification of tariff refund claims or auditor-level convergence in recovery accounting. No directly matching accounting working paper was identified in the returned tariff-refund search, but the SSRN results were noisy. |
| **Novel angle** | Links a new recovery setting to a manually validated disclosure-to-recognition-to-cash sequence, separating accounting uncertainty from collection delay. The proposed contribution is not simply that tariffs affect earnings. |
| **Accounting angle** | Directly examines recognition versus disclosure, inventory and cost-of-sales effects, presentation of nonrecurring income, and consistency of accounting judgments across audit clients. |
| **Identification** | Begin with descriptive transition analysis and within-firm recognition hazards around verified administrative milestones. Estimate exposure-by-post specifications using tariff exposure measured from pre-April 20 filings, industry-by-quarter effects, and pretrend tests. Compare accounting choices among firms with similar disclosed claim status and original tariff-cost treatment. Auditor-portfolio convergence is an association unless auditor assignment or clarification timing supplies independently defensible variation; CAPE submission and payment dates must not be treated as exogenous. |
| **Risks** | Recognition choices may reflect legitimately different facts rather than discretion. The common launch is not a randomized shock, actual refund eligibility may be unobservable, and the SSRN search returned weakly relevant results. Do not claim a causal auditor effect or definitive absence of competing work. |

**Hypotheses**
- H1: Firms disclose refund claims before recognizing earnings benefits when eligibility or recovery remains uncertain.
- H2: Recognition-policy and presentation similarity increase within auditor portfolios after common administrative clarification.
- H3: Recognition before cash collection is associated with more specific explanations of the evidence supporting recognition.
- H4: Reported gross-margin effects differ with whether the related tariff costs remain in inventory or were previously expensed.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), Audit Analytics, CRSP Stock / Security Files
- **Disclosure text:** SEC EDGAR 10-Q and 10-K inventory, contingencies, and accounting-policy footnotes, SEC EDGAR MD&A discussions of tariff refunds, SEC EDGAR 8-K earnings-release exhibits
- **Sample:** U.S. listed operating companies, 2024–October 20, 2026 for the initial panel; future 2026–2027 filings needed for complete collection and reversal outcomes.
- **Key variables:**
  - Refund disclosure: manually validated indicator and disclosed claim amount, scaled by lagged assets.
  - Recognition: first explicit recognized receivable or income effect; code uncertainty rather than infer recognition from a generic tariff mention.
  - Classification: inventory adjustment, cost of sales, other income, interest income, or unclassified.
  - Collection: first explicitly reported cash receipt and amount; distinguish receipt from claim submission or approval.
  - Ex ante exposure: pre-April 20, 2026 disclosed tariff costs or import dependence; preserve missing amounts as missing.
  - Auditor coordination: leave-one-out recognition-policy similarity within audit-firm portfolios.
  - Controls: size, profitability, inventory intensity, leverage, industry, fiscal-quarter timing, and auditor.
- **EDGAR check:** Query "tariff refunds"; forms 10-K,10-Q; April 20–October 20, 2026: 512 returned hits; total_is_lower_bound=false. The returned sample contained 100 unique filings, not 100 verified eligible firms. Hits can include exhibits and repeated documents and are rough upper bounds on usable observations.
- **Feasibility notes:** All proposed WRDS subscriptions are cataloged as assumed, not confirmed. EDGAR is free. Claim-level ACE records are not assumed available and are not required. Main risks are missing recognized amounts, endogenous administrative timing, inventory accounting heterogeneity, and a short outcome window. Proceed only after a 50-firm pilot establishes sufficient explicit recognition disclosures.

</details>

<details><summary><b>News triggers</b></summary>

- [CSMS # 68536553 - CBP Offers Multiple ACE Reports for Monitoring CAPE Refund Claims](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/415c8e9?reqfrom=share) — U.S. Customs and Border Protection, 2026-05-04

</details>

<details><summary><b>Related papers</b></summary>

- The Impact of Recognition Versus Disclosure on Financial Information: A Preparer's Perspective (Shana M. Clor-Proell, Laureen A. Maines, 2014, Journal of Accounting Research)
- Mandatory disclosure and asymmetry in financial reporting (Jeremy Bertomeu, Robert P. Magee, 2014, Journal of Accounting and Economics)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 09:09 — 20261020_090932_open_scan_of_financial_reporting_disclosure_auditi

</details>

</details>

<a id="i-002"></a>
<details><summary><b>I-002 · 2. The Unexplained Remainder: Residual Aggregation under the New Income Tax Disclosures</b></summary>

**Novelty** ★★☆☆☆ · **Data feasibility** `medium` · first seen 2026-10-20 09:09 · last updated 2026-10-20 09:09

> **Research question.** Does residual aggregation under ASU 2023-09 obscure the connection between tax expense, jurisdictional tax effects, and cash taxes paid?

| | |
|---|---|
| **What it is** | Measure the share of tax information remaining aggregated after the first ASU 2023-09 disclosures, rather than repeat a generic market-reaction study. The May 2 practitioner report describes first-year adoption, while the April 29 OECD–USCIB announcement explicitly identifies enhanced FASB tax disclosures as a conference topic. Separate the rate-reconciliation threshold from the cash-taxes-paid threshold and investigate whether residual aggregation limits reconciliation of tax expense to cash payments. ([sw-cpas.com](https://sw-cpas.com/asu-2023-09-income-tax-disclosures-fortune-500-first-year/?utm_source=openai)) |
| **Gap** | 10.2139/ssrn.5542138 already studies anticipatory stock-market and reporting responses, and 10.2139/ssrn.7355339 already studies investor reactions to first jurisdiction-level disclosures. 10.1007/s11142-026-09962-3 relates numeric tax disclosure to ETR forecasting. The narrower proposed gap is the unexplained residual and cross-table reconciliation, not the general value of tax transparency. The two working papers materially constrain novelty. ([papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5542138&utm_source=openai)) |
| **Novel angle** | A reproducible accounting measure connecting named jurisdictions, residual categories, tax-rate reconciliation, and cash taxes paid. The design explicitly avoids claiming a regression discontinuity when undisclosed below-threshold jurisdiction amounts cannot be observed. |
| **Accounting angle** | Examines footnote completeness, quantitative disaggregation, comparability, and the informational content of disclosure-only accounting standards. |
| **Identification** | Primary design is a disclosure-measurement study with within-firm comparisons across adoption and, prospectively, the second adoption year. Use fiscal-year adoption timing only after testing seasonality and concurrent tax-law confounds. Estimate associations conditional on pre-adoption disclosure, foreign operations, losses, and tax complexity. No causal threshold design or bunching claim is warranted without independently observed jurisdiction-level amounts below the disclosure threshold. |
| **Risks** | High overlap with Anticipating Change and The Value of Tax Transparency. Residual categories can be economically appropriate. Foreign cash taxes and foreign rate effects measure different constructs, so unmatched jurisdictions are not evidence of error. Do not infer manipulation or noncompliance from residual aggregation alone. |

**Hypotheses**
- H1: Larger residual shares are associated with less stable year-to-year jurisdictional tax disclosure.
- H2: Firms with larger residual shares provide more supplemental narrative explanation when tax expense and cash taxes diverge.
- H3: Residual aggregation is associated with larger subsequent ETR forecast revisions, conditional on overall numeric disclosure volume.
- H4: Within-firm reductions in residual aggregation improve cross-table reconciliation more than increases in narrative length.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), Compustat Segments, I/B/E/S, Audit Analytics
- **Disclosure text:** SEC EDGAR 10-K income-tax rate-reconciliation tables, SEC EDGAR 10-K cash-taxes-paid tables and accompanying explanations, SEC EDGAR Exhibit 21 subsidiary lists
- **Sample:** U.S. listed public business entities with usable income-tax footnotes, fiscal years 2023–2025 and fiscal-2026 reports available by October 20, 2026; second-year tests require later filings.
- **Key variables:**
  - Cash-tax residual: disclosed total net cash taxes paid less separately quantified jurisdictions, avoiding double-counting federal/state/foreign subtotals.
  - Rate-reconciliation residual: absolute unallocated reconciling effects divided by a prespecified gross absolute-effects denominator; report signed and absolute variants.
  - Cross-table linkage: proportion of named jurisdictions with interpretable information in both tables; absence is not automatically noncompliance.
  - Threshold coding: rate-reconciliation threshold uses statutory tax on pretax income or loss; cash-tax jurisdiction threshold uses total income taxes paid net of refunds.
  - Numeric disclosure volume and explanatory narrative volume: separate table cells and text, with hand validation.
  - Optional ETR forecast outcome: use I/B/E/S only if compatible pretax and after-tax forecasts are available; otherwise omit rather than substitute EPS dispersion.
  - Controls: foreign sales, pretax losses, deferred taxes, unrecognized tax benefits when explicitly disclosed, size, auditor, and prior disclosure detail.
- **EDGAR check:** Query "2023-09"; form 10-K; April 20–October 20, 2026: 608 returned hits; total_is_lower_bound=false; 99 unique filings in the returned sample. These are mentions, often new-standard discussions, not verified compliant tax tables. The final sample must search earlier 2026 filings as well.
- **Feasibility notes:** All WRDS subscriptions are assumed, not confirmed. Tables are publicly available but require extensive parsing and reconciliation. The 608 hits do not establish an adopter count. A second-year panel is incomplete at the cutoff. I/B/E/S pretax forecast coverage must be established before committing to forecast tests. Close working papers create substantial scoop risk.

</details>

<details><summary><b>News triggers</b></summary>

- [ASU 2023-09 Income Tax Disclosures: Fortune 500 First-Year Adoption](https://sw-cpas.com/asu-2023-09-income-tax-disclosures-fortune-500-first-year/) — SW Accounting & Consulting Corp, 2026-05-02
- [Save the Date: Annual OECD–USCIB International Tax Conference](https://uscib.org/save-the-date-annual-oecd-uscib-international-tax-conference/) — United States Council for International Business, 2026-04-29

</details>

<details><summary><b>Related papers</b></summary>

- Voluntary Disclosure Responses to Mandated Disclosure: Evidence from Australian Corporate Tax Transparency (Allison Kays, 2021, The Accounting Review)
- Tax numbers and ETR forecasting (Carlyle S. Burd, 2026, Review of Accounting Studies)
- Tax Strategy Disclosure: A Greenwashing Mandate? (Katarzyna Bilicka, Elisa Casi-Eberhard, Carol Seregni, 2025, Journal of Accounting Research)
- Anticipating Change: Stock Market and Firm Responses to Disaggregation in Income Tax Disclosures (Derek Christensen, Dan Lynch, Anh Nguyen, 2025, SSRN; also presented at 2026 FARS and EAA meetings)
- The Value of Tax Transparency (Jaron H. Wilde, Ryan J. Wilson, Joshua Wiseman, 2026, SSRN)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 09:09 — 20261020_090932_open_scan_of_financial_reporting_disclosure_auditi

</details>

</details>

<a id="i-003"></a>
<details><summary><b>I-003 · 3. Quality-Control Compliance Costs and Small-Auditor Client Retention</b></summary>

**Novelty** ★★★★☆ · **Data feasibility** `low` · first seen 2026-10-20 09:09 · last updated 2026-10-20 09:09

> **Research question.** Do fixed quality-control implementation costs cause small auditors to raise fees, shed clients, or exit issuer auditing, and do cost-reducing amendments mitigate those responses?

| | |
|---|---|
| **What it is** | Study whether QC 1000 implementation costs change audit fees, client retention, and audit-market participation among small audit firms, and whether these effects are moderated by pre-existing quality-control arrangements. The PCAOB adopted amendments on September 9, 2026 intended to reduce compliance costs, including eliminating the design-only requirement and increasing staffing flexibility. This is a prospective study: QC 1000 is scheduled to take effect December 15, 2026, and the September amendments require SEC approval. ([pcaobus.org](https://pcaobus.org/oversight/standards/standard-setting-research-rulemaking-related-activities/quality-control?utm_source=openai)) |
| **Gap** | 10.1111/1475-679x.12151 examines remediation after inspection deficiencies and finds fee and internal-control reporting responses. 10.2308/ajpt-50752 examines reputation following public QC criticisms. These are not tests of the fixed-cost effects of an ex ante system-design mandate and subsequent regulatory relief. ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/abs/10.1111/1475-679X.12151?utm_source=openai)) |
| **Novel angle** | Connects quality-control regulation to extensive-margin audit supply and client reallocation rather than assuming every fee increase represents better audit quality. |
| **Accounting angle** | Directly concerns audit regulation, audit supply, fees, engagement continuity, and the trade-off between compliance costs and assurance quality. |
| **Identification** | Pre-register a continuous-exposure event study using 2024–2025 issuer portfolio size, pre-rule public QC information, and client mix. Use auditor and client fixed effects and pretrend tests; cluster at the audit-firm level. Distinguish anticipation after the original rule, the 2025 postponement, the June 2026 amendment proposal, September adoption, and actual implementation. This is not a clean treated-versus-untreated experiment because most active issuer auditors face the rule and exposure correlates with scale. Do not use nonpublic Form QC conclusions as outcomes. |
| **Risks** | Future-data dependence, SEC-approval uncertainty for the September amendments, endogenous audit-firm size, concurrent audit-market consolidation, and sparse pre-existing QC disclosures. The QC SSRN search was uninformative and the Semantic Scholar cross-check was rate-limited, so the novelty assessment is provisional. |

**Hypotheses**
- H1: Implementation-related fee increases are larger for clients of auditors with fewer pre-rule issuer engagements.
- H2: Small auditors with weakly documented pre-existing QC infrastructure are more likely to reduce issuer-client portfolios.
- H3: Client reallocations are concentrated among economically small engagements.
- H4: Any implementation-related improvement in adverse internal-control reporting is stronger where the auditor had greater pre-rule inspection deficiencies.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Audit Analytics, Compustat North America (Fundamentals Annual/Quarterly)
- **Disclosure text:** SEC EDGAR DEF 14A audit-fee and audit-committee disclosures, SEC EDGAR 8-K Item 4.01 auditor changes, SEC EDGAR 10-K audit reports and internal-control opinions
- **Sample:** U.S. issuer-auditor engagements, 2022–October 20, 2026 for baseline and anticipation analysis; prospective 2027–2029 outcomes required.
- **Key variables:**
  - Audit fees: log fees and fee growth from Audit Analytics, reconciled to proxy disclosures.
  - Pre-rule portfolio scale: issuer audit-client count from available auditor-client links; validate audit-firm legal-entity matching.
  - Client retention and exit: auditor changes and persistent disappearance from issuer auditing, requiring subsequent observations.
  - QC gap: pre-rule public inspection criticisms and publicly documented QC arrangements; not inferred from nonpublic Form QC.
  - Quality outcomes: adverse internal-control opinions, subsequent restatements, and audit-report lag.
  - Controls: client assets, complexity, losses, leverage, industry, auditor tenure, and merger indicators.
- **EDGAR check:** Query "quality control"; forms 10-K,DEF 14A; April 20–October 20, 2026: 593 returned hits; total_is_lower_bound=false; 100 unique filings in the returned sample. Many hits concern product quality or exhibits. This is only a generic text-availability screen and does not establish QC 1000 treatment coverage.
- **Feasibility notes:** WRDS access is assumed. No post-implementation outcomes exist by the stated cutoff. Core fees and auditor-change data are feasible, but public PCAOB inspection reports and firm-identity validation require supplementary collection. Form QC is nonpublic. The design is suitable for pre-registration, not a completed causal implementation paper today.

</details>

<details><summary><b>News triggers</b></summary>

- [PCAOB Adopts Amendments to Its Quality Control Standard](https://pcaobus.org/oversight/standards/standard-setting-research-rulemaking-related-activities/quality-control) — PCAOB, 2026-09-09

</details>

<details><summary><b>Related papers</b></summary>

- Do PCAOB Inspections Improve the Quality of Internal Control Audits? (Mark L. DeFond, Clive S. Lennox, 2017, Journal of Accounting Research)
- PCAOB Quality Control Inspection Reports and Auditor Reputation (Albert L. Nagy, 2014, Auditing: A Journal of Practice & Theory)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 09:09 — 20261020_090932_open_scan_of_financial_reporting_disclosure_auditi

</details>

</details>

<a id="i-004"></a>
<details><summary><b>I-004 · 4. Climate Disclosure Retrenchment or Relocation into Financial Reporting?</b></summary>

**Novelty** ★★☆☆☆ · **Data feasibility** `medium` · first seen 2026-10-20 09:09 · last updated 2026-10-20 09:09

> **Research question.** Does reduced expected climate-specific regulation change where financially material climate information appears, rather than only how much climate language firms use?

| | |
|---|---|
| **What it is** | Test whether firms reduce highly visible climate terminology while preserving or expanding financially quantified climate information in MD&A and accounting footnotes after the SEC's May 29, 2026 rescission proposal. Measure movement across sections within the same filing rather than interpret a falling climate-word count as falling disclosure quality. The event is a proposal to rescind the rules, not evidence that an operative disclosure mandate was removed on that date. ([sec.gov](https://www.sec.gov/files/33-11421-fact-sheet.pdf?utm_source=openai)) |
| **Gap** | 10.1093/rfs/hhad002 establishes investor demand for climate disclosure; 10.1007/s11142-021-09611-x studies a mandate's real effects. Crucially, 10.2139/ssrn.7220660 already documents ESG camouflage and later substantive retrenchment using 2020–2025 10-Ks. The remaining candidate contribution is section-level relocation into quantified accounting information following the specific 2026 proposal, not a new discovery of camouflage. ([accounting-for-transparency.de](https://www.accounting-for-transparency.de/de/publications/no-244-staying-under-the-radar-the-case-of-sustainability-disclosures-in-the-us/?utm_source=openai)) |
| **Novel angle** | A within-document linkage measure distinguishing politically salient labels from quantified accounting consequences; conditional on demonstrating that the frontier paper does not already implement the same measure. |
| **Accounting angle** | Studies the integration of narrative risk disclosure with impairment, useful-life, contingency, and expenditure disclosures in financial reporting. |
| **Identification** | Use within-firm, section-by-period comparisons and pre-event exposure to the original rule's expected requirements. Include industry-by-period effects and pretrends. Analyze the May 29 proposal as an expectations event, with alternative dates and anticipation tests. Exposure based on foreign or state obligations requires independently verified applicability; geographic sales alone cannot establish legal coverage. Without a credible control group, frame results as disclosure reallocation associations rather than a causal repeal effect. |
| **Risks** | High overlap with Staying under the radar. The 2026 FARS program also contains related climate-disclosure oversight and emissions-reporting work. A new event date alone is insufficient novelty. The proposal may have been anticipated, and word relocation can be mechanical rather than informative. |

**Hypotheses**
- H1: Politically salient climate terminology declines more than financially quantified climate information.
- H2: Firms with stronger pre-event investor demand preserve accounting-linked climate information more often.
- H3: A subset of firms relocates information from stand-alone risk discussion to asset, expenditure, or contingency discussion.
- H4: Apparent disclosure reductions based on word counts overstate reductions based on validated accounting-linked information.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), Compustat Segments, Thomson/Refinitiv 13F Institutional Holdings, Audit Analytics
- **Disclosure text:** SEC EDGAR 10-K Item 1A, SEC EDGAR 10-K Item 7 MD&A, SEC EDGAR asset, impairment, contingency, and accounting-estimate footnotes, SEC EDGAR 10-Q updates
- **Sample:** U.S. listed operating firms with comparable filings, 2022–October 20, 2026; a complete calendar-year 2026 annual-report test requires 2027 filings.
- **Key variables:**
  - Label intensity: frequency of climate and ESG labels, reported separately from substance.
  - Accounting-linked information: human-validated passages connecting climate-related conditions to a quantified financial amount or explicit accounting estimate.
  - Relocation: matched topics disappearing from risk factors but remaining or appearing in MD&A or footnotes.
  - Quantification: monetary amounts, useful-life changes, impairment amounts, or expenditure commitments explicitly connected to the topic.
  - Investor demand: pre-event institutional ownership composition, without assuming 13F identifies climate preferences.
  - Controls: industry, size, asset intensity, losses, foreign sales, filing length, and contemporaneous physical-risk disclosures.
- **EDGAR check:** Query "climate-related"; forms 10-K,10-Q; April 20–October 20, 2026: 624 returned hits; total_is_lower_bound=false; 98 unique filings in the returned sample. SPAC boilerplate and exhibits appear among results. This is a phrase screen, not a census of financially material climate disclosures.
- **Feasibility notes:** WRDS access is assumed. Free EDGAR permits initial measurement development. Low base rates of explicitly quantified climate-related accounting passages, incomplete annual post-event coverage, and extensive hand validation are principal risks. No commercial ESG dataset outside the catalog is assumed.

</details>

<details><summary><b>News triggers</b></summary>

- [Fact Sheet: Rescission of Climate-Related Disclosure Rules](https://www.sec.gov/files/33-11421-fact-sheet.pdf) — SEC, 2026-05-29

</details>

<details><summary><b>Related papers</b></summary>

- Climate Risk Disclosure and Institutional Investors (Emirhan Ilhan, Philipp Krueger, Zacharias Sautner, 2023, Review of Financial Studies)
- The impact of carbon disclosure mandates on emissions and financial operating performance (Benedikt Downar, Jürgen Ernstberger, Stefan Reichelstein, 2021, Review of Accounting Studies)
- Staying under the radar: The case of sustainability disclosures in the US (Khrystyna Bochkay, Thorsten Sellhorn, Katharina J. Weiß, 2026, SSRN; TRR 266 Accounting for Transparency Working Paper No. 244)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 09:09 — 20261020_090932_open_scan_of_financial_reporting_disclosure_auditi

</details>

</details>

<a id="i-005"></a>
<details><summary><b>I-005 · 5. Voluntary Quarterly Disclosure as a Commitment When Mandatory Frequency Is Uncertain</b></summary>

**Novelty** ★★☆☆☆ · **Data feasibility** `low` · first seen 2026-10-20 09:09 · last updated 2026-10-20 09:09

> **Research question.** Which firms voluntarily commit to quarterly information production when mandatory reporting frequency may decline, and how credible are those commitments?

| | |
|---|---|
| **What it is** | Study whether firms publicly commit to maintaining quarterly earnings information when regulators propose allowing less frequent mandatory reports. The May 5 proposal would allow a new semiannual Form 10-S in place of three Forms 10-Q if adopted; it does not itself establish a realized switch. The immediately feasible project is commitment disclosure and anticipation, while a later extension could examine whether earnings releases substitute for reduced mandatory filings. ([sec.gov](https://www.sec.gov/newsroom/speeches-statements/atkins-statement-proposing-release-semiannual-reporting-050526?utm_source=openai)) |
| **Gap** | 10.2308/accr-51936 studies bank reporting frequency and loan quality; 10.2308/tar-2017-0550 studies complementarity between audited reporting and voluntary disclosure. 10.2139/ssrn.5481486 directly addresses reporting frequency and reporting quality, while 10.2139/ssrn.7039063 addresses managerial discretion over reporting frequency. The proposed distinction is an explicit, observable commitment to preserve information, not another generic frequency-quality study. |
| **Novel angle** | Separates preserving quarterly earnings announcements from preserving quarterly GAAP statements, review assurance, detailed footnotes, and management forecasts. A commitment is coded only from explicit forward-looking statements. |
| **Accounting angle** | Distinguishes mandatory financial statements, voluntary earnings releases, management forecasts, and commitment to a reporting cadence. |
| **Identification** | As of the cutoff, use a hand-validated commitment-choice design and proposal-window event study, conditioning on pre-proposal reporting practices. Treat commitment choice as endogenous. Only if adoption and actual elections are subsequently verified should the project add an adoption analysis; voluntary switchers versus nonswitchers are not automatically valid DiD treatment and control groups. |
| **Risks** | Close overlap with Less is More? and Should Regulators Allow Public-Firm Managers to Unilaterally Reduce Reporting Frequency? Their abstracts were not recovered, preventing a complete overlap assessment. Proposal anticipation, endogenous commitments, a potentially tiny sample, and uncertain future regulatory timing make this a watch-list idea. |

**Hypotheses**
- H1: Firms with greater pre-event analyst coverage are more likely to commit explicitly to continued quarterly disclosure.
- H2: Commitments are more specific when firms have a history of regular, detailed voluntary earnings releases.
- H3: Commitments to earnings releases are more common than commitments to preserve the full quarterly financial-reporting package.
- H4: Subsequent disclosure consistency is higher for specific commitments than for generic transparency statements.

<details><summary><b>Data plan</b></summary>

- **WRDS:** Compustat North America (Fundamentals Annual/Quarterly), CRSP Stock / Security Files, I/B/E/S, Thomson/Refinitiv 13F Institutional Holdings
- **Disclosure text:** SEC EDGAR 8-K Item 2.02 and earnings-release exhibits, SEC EDGAR 10-K and 10-Q reporting-policy statements, SEC EDGAR 8-K investor-presentation exhibits
- **Sample:** U.S. domestic listed issuers, 2023–October 20, 2026 for baseline and commitment collection. Actual reporting-frequency changes are a conditional future extension, not an observed treatment assumed here.
- **Key variables:**
  - Explicit commitment: preserve quarterly earnings releases, quarterly financial statements, forecasts, or reviewed statements; code these separately.
  - Specificity: named cadence, content, and duration rather than generic transparency language.
  - Baseline disclosure: quarterly release regularity, financial-statement content, quantitative guidance, and footnote detail.
  - Information environment: analyst coverage and institutional ownership measured before May 5, 2026.
  - Optional market outcome: short-window abnormal returns around the first explicit commitment, excluding confounding earnings announcements where possible.
  - Controls: size, losses, financing needs, volatility, reporting history, fiscal-year end, and industry.
- **EDGAR check:** Query "quarterly results"; form 8-K; April 20–October 20, 2026: 647 returned hits; total_is_lower_bound=false; 95 unique filings in the returned sample. This establishes availability of earnings-release text only. It does not count commitments or semiannual elections.
- **Feasibility notes:** WRDS subscriptions are assumed. Explicit commitment statements may be rare and are not established by the EDGAR screen. No final adoption or realized issuer elections were verified in this scan. Require a dedicated commitment-phrase pilot before proceeding; abandon the archival commitment study if the treated sample is too small.

</details>

<details><summary><b>News triggers</b></summary>

- [Statement on Proposing Release for Semiannual Reporting](https://www.sec.gov/newsroom/speeches-statements/atkins-statement-proposing-release-semiannual-reporting-050526) — SEC, 2026-05-05

</details>

<details><summary><b>Related papers</b></summary>

- Banks' Financial Reporting Frequency and Asset Quality (Karthik Balakrishnan, Aytekin Ertan, 2017, The Accounting Review)
- Complementarity between Audited Financial Reporting and Voluntary Disclosure: The Case of Former Andersen Clients (Richard M. Frankel, Alon Kalay, Gil Sadka, 2021, The Accounting Review)
- Less is More? The Effect of Reporting Frequency on Financial Reporting Quality (Sam Islam, Clark M. Wheatley, 2025, SSRN)
- Should Regulators Allow Public-Firm Managers to Unilaterally Reduce Reporting Frequency? (Jesse M. Fried, 2026, SSRN)

</details>
<details><summary><b>Version history</b></summary>

- 2026-10-20 09:09 — 20261020_090932_open_scan_of_financial_reporting_disclosure_auditi

</details>

</details>

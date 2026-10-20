# Research Idea Bank
_Run 2026-10-20 09:09 · topic: Open scan of financial reporting, disclosure, auditing, and tax research opportunities; information cutoff October 20, 2026; news window April 20–October 20, 2026._

**5 new · 0 updated · 5 ideas in bank · 16 papers reviewed in total**

## Overview

| ID | This run | Idea | Novelty | Data | Last updated |
|---|---|---|---|---|---|
| I-001 | 🆕 new | [1. From Tariff Refund Claims to Reported Earnings: Recognition, Classification, and Auditor Coordination](#i-001) | 4/5 | medium | 2026-10-20 09:09 |
| I-002 | 🆕 new | [2. The Unexplained Remainder: Residual Aggregation under the New Income Tax Disclosures](#i-002) | 2/5 | medium | 2026-10-20 09:09 |
| I-003 | 🆕 new | [3. Quality-Control Compliance Costs and Small-Auditor Client Retention](#i-003) | 4/5 | low | 2026-10-20 09:09 |
| I-004 | 🆕 new | [4. Climate Disclosure Retrenchment or Relocation into Financial Reporting?](#i-004) | 2/5 | medium | 2026-10-20 09:09 |
| I-005 | 🆕 new | [5. Voluntary Quarterly Disclosure as a Commitment When Mandatory Frequency Is Uncertain](#i-005) | 2/5 | low | 2026-10-20 09:09 |

## New and updated ideas this run

---

<a id="i-001"></a>
### I-001 · 1. From Tariff Refund Claims to Reported Earnings: Recognition, Classification, and Auditor Coordination (🆕 new)
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

---

<a id="i-002"></a>
### I-002 · 2. The Unexplained Remainder: Residual Aggregation under the New Income Tax Disclosures (🆕 new)
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

---

<a id="i-003"></a>
### I-003 · 3. Quality-Control Compliance Costs and Small-Auditor Client Retention (🆕 new)
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

---

<a id="i-004"></a>
### I-004 · 4. Climate Disclosure Retrenchment or Relocation into Financial Reporting? (🆕 new)
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

---

<a id="i-005"></a>
### I-005 · 5. Voluntary Quarterly Disclosure as a Commitment When Mandatory Frequency Is Uncertain (🆕 new)
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

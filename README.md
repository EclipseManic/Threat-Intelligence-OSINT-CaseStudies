# Threat Intelligence and OSINT Case Studies

Four evidence-led investigations into cybercrime markets, exploit claims, state-linked threat activity, and brand exposure.

These case studies began as solutions to a take-home threat-intelligence assessment. I independently collected and evaluated public evidence, developed the analytical judgments, and later expanded the work into a portfolio because the research was challenging, practical, and valuable to my development as an analyst.

## Start Here

Each case study answers a different intelligence question. The short finding below provides the conclusion before the detailed evidence.

| Case study | Intelligence question | Plain-English finding |
|---|---|---|
| [Underground Threat Economy](case-studies/01-underground-threat-economy/) | How do cybercrime markets divide an intrusion into services? | Access, credentials, malware delivery, stolen data, and cash-out are sold separately. Individual listings are unreliable, but the service economy materially lowers attacker cost. |
| [Exploit-Claim Credibility](case-studies/02-exploit-claim-credibility/) | Was an advertised Android exploit really a fresh zero-day chain? | Probably not. The strongest explanation is repackaged or incomplete public-vulnerability code with exaggerated escape claims. |
| [Handala Threat Actor](case-studies/03-handala-threat-actor/) | Is Handala an independent hacktivist group or a state-linked persona? | The evidence better supports an Iran-linked state or state-directed operation, but the specific MOIS attribution is less certain. |
| [Brand Exposure Monitoring](case-studies/04-brand-exposure-monitoring/) | Did public monitoring reveal a verified Nykaa exposure or impersonation campaign? | No verified current incident was found. RDAP and public-suffix analysis also showed that several initially suspicious domains were likely defensive or incorrectly classified. |

Readers unfamiliar with terms such as RaaS, RDAP, IOC, or n-day can use the [plain-language glossary](GLOSSARY.md).

## Evidence And Verification

The [public evidence index](evidence/) maps representative source excerpts to specific findings. A SHA-256 manifest also records the private originals, allowing them to be verified later without publishing raw forum captures, personal data, or restricted material.

This evidence model provides three levels of verification:

1. Public screenshots show representative collection and visible source context.
2. Source URLs and dates allow a reviewer to inspect the underlying public reporting.
3. Cryptographic hashes allow privately shared originals to be matched to the files used during analysis.

## What This Project Demonstrates

| Skill | Where it appears |
|---|---|
| Source evaluation and confidence | Every case distinguishes direct observation, third-party reporting, claims, and inference |
| Competing hypotheses | Exploit credibility and Handala attribution studies |
| MITRE ATT&CK and Diamond Model | Handala threat-actor study |
| Underground-market analysis | Marketplace, RaaS, initial-access broker, and forum comparison |
| Passive infrastructure research | DNS, PTR, RDAP, registration chronology, and public-suffix analysis |
| Correcting analytical mistakes | Escrow interpretation, unsupported ATT&CK mapping, attribution confidence, and domain false positives |
| Defensive communication | Every report ends with proportionate actions and limitations |

Original assessment prompts and scoring material are not reproduced. Each case study contains a paraphrased research objective, methodology, evidence assessment, limitations, and defender-focused conclusions.

## How To Read The Analysis

- **Observed** means I directly viewed the public page or metadata.
- **Reported** means a named source made the statement.
- **Claimed** means a seller, threat actor, or leak site made the allegation.
- **Assessed** means the conclusion is my interpretation of the available evidence.

Confidence measures evidence quality, not potential impact. A severe scenario can still be Low confidence when proof is weak.

## Research Boundaries

All collection was passive and limited to publicly accessible sources. No unauthorised access, threat-actor interaction, purchase, malware execution, exploitation, or download of leaked data was performed. Indicators are defanged, personal information is excluded, and unverified claims are labelled as such.

See [ETHICS.md](ETHICS.md) for the full research and publication policy.

## Repository Structure

```text
case-studies/   Public analytical reports
methodology/    Collection, source-grading and confidence framework
tools/          Safe passive-OSINT utilities and PDF builder
pdf/            Generated portfolio PDFs
assets/         Redacted public assets only
evidence/       Claim-to-source indexes and integrity manifest
GLOSSARY.md     Plain-language explanation of specialist terms
```

The Markdown reports are the canonical public source. PDFs are generated from them with `python tools/build_portfolio.py`.

## Reproducibility

- Public sources and collection dates are identified in each case study.
- Dynamic infrastructure findings are presented as timestamped snapshots.
- The included DNS/PTR utility reproduces the collection method without opening candidate websites.
- PDFs are generated directly from the public Markdown source.
- Negative findings are limited to the source and collection time; they are never presented as proof of absence.

## Downloadable PDFs

- [Underground Threat Economy](pdf/01%20-%20Underground%20Threat%20Economy.pdf)
- [Exploit Claim Credibility](pdf/02%20-%20Exploit%20Claim%20Credibility.pdf)
- [Handala Threat Actor](pdf/03%20-%20Handala%20Threat%20Actor.pdf)
- [Brand Exposure Monitoring](pdf/04%20-%20Brand%20Exposure%20Monitoring.pdf)

## Authorship And Assistance

Research ownership, source collection, and analyst direction: **Manichand Gupta**. AI-assisted tools were used for editorial restructuring, analytical review, document generation, consistency checks, and quality assurance.

## Disclaimer

This is an independent educational portfolio project. It is not affiliated with or endorsed by the organisation that supplied the original assessment. Findings reflect publicly available information at the stated collection dates and should not be treated as current operational intelligence without revalidation.

## Licence

Original written analysis is licensed under [CC BY 4.0](LICENSE.md). Code in `tools/` is licensed separately under the MIT License. Third-party source material and quoted or captured excerpts remain the property of their respective owners.

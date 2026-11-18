# Methodology

## Intelligence Cycle

1. **Define the question.** Specify what decision the research should support and what would count as a material finding.
2. **Set collection boundaries.** Record allowed sources, prohibited interaction, time window, and stop conditions.
3. **Establish a baseline.** Identify legitimate domains, infrastructure, official personas, and expected behaviour before classifying anomalies.
4. **Collect minimally.** Preserve the smallest evidence excerpt needed; do not retain leaked records or credentials.
5. **Separate evidence layers.** Distinguish direct observation, third-party reporting, actor claim, and analyst inference.
6. **Test alternatives.** Develop competing hypotheses and record evidence for and against each.
7. **Calibrate confidence.** Base confidence on source quality, independence, recency, directness, and consistency.
8. **Translate to action.** Pair severity with confidence so collection gaps are not mistaken for confirmed incidents.
9. **Review and correct.** Re-run dynamic checks, test timelines, identify circular reporting, and remove unsupported mappings.

## Collection Standard

- Passive and public sources only
- No unauthorised authentication or access
- No threat-actor engagement or purchases
- No malware, exploit, credential, or leaked-dataset downloads
- UTC timestamps for evidence and queries
- Defanged infrastructure in reports
- Negative results scoped to the source and collection time

## Evidence Labels

| Label | Meaning |
|---|---|
| Observed | The analyst directly viewed the public page or metadata |
| Reported | A named source states the claim |
| Claimed | A seller, actor, or leak site makes the allegation |
| Inferred | The analyst derives a conclusion from multiple facts |
| Unknown | Evidence does not support a defensible conclusion |

Direct observation proves that content existed at collection time. It does not automatically validate the underlying allegation.

## Confidence Scale

| Level | Standard |
|---|---|
| High | Multiple independent, direct, technically consistent sources; limited plausible alternatives |
| Moderate | Credible evidence with material gaps, partial dependence, or unresolved alternatives |
| Low | Single-source, indirect, stale, contradictory, or actor-controlled evidence |
| Unknown | Insufficient evidence to assess |

Confidence measures evidential support, not severity. A high-impact scenario can remain Low confidence.

## Severity And Priority

Severity and confidence are assessed separately:

- **Severity:** potential operational, financial, legal, or safety impact
- **Confidence:** strength of evidence that the condition exists
- **Priority:** action required given both factors and the cost of validation

An unverified high-impact scenario generally triggers rapid validation, not immediate attribution or takedown.

## Source Independence

Ten articles repeating one vendor report count as one evidence lineage. Research logs therefore record the earliest identifiable source, which claims were copied, and whether another source adds independent technical or victim confirmation.

## Dynamic Infrastructure

DNS, CDN addresses, certificates, registration data, parking pages, and social accounts change. A script reproduces a method, not an old result. Every dynamic claim should carry a timestamp and be revalidated before operational use.

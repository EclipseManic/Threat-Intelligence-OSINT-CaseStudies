# Underground Threat Economy

**Public Portfolio Case Study | TLP:CLEAR**

| | |
|---|---|
| Analyst | Manichand Gupta |
| Research period | October-November 2026 |
| Methods | Passive OSINT, source grading, tracker analysis, confidence calibration |
| Safety | No purchases, actor contact, leaked-data download, or malware retrieval |

## Challenge

Map how underground cybercrime markets separate intrusion into purchasable services, compare ransomware operating models, examine forum trust cultures, and turn the evidence into defensible intelligence judgments. The original assessment prompt is not reproduced.

## In Plain English

Modern cybercrime often works like a supply chain. One person steals credentials, another sells network access, another provides malware, and another converts the proceeds. This specialisation makes attacks easier to launch, even though many individual advertisements remain exaggerated, false, or impossible to verify.

## Executive Assessment

The underground economy reduces the expertise needed for intrusion by separating access, delivery, stolen identity material, data, and value transfer into services. The strongest defensive conclusion is not that every listing is genuine, but that reusable credentials, session tokens, exposed remote services, and brokered access reduce attacker cost even when individual marketplace claims are unreliable.

The evidence supported three distinct ransomware structures: Qilin as an affiliate-led service, SafePay as a reported internal operation, and Play as a presumed closed group with broker relationships. Similar leak-site activity therefore does not imply identical internal structure or repeatable tradecraft.

Confidence is Moderate. Most evidence came from government, vendor, academic, news, and tracker reporting. Direct observations established that posts or services existed, not that every seller claim was true.

## Collection Boundaries

- Isolated virtual machine with NAT, VPN/Tor where appropriate
- Public, no-login access only
- No registration, messaging, negotiation, transaction, or download
- No leaked data or credentials retained
- Actor-controlled indicators defanged in notes
- Claims separated into observed, reported, and inferred layers

An early collection item that did not meet the defined environment standard was excluded and replaced with a no-login public landing page. This correction mattered because collection quality includes how evidence was obtained, not only what it appears to show.

## Marketplace Taxonomy

| Category | Dated example | Intelligence value | Confidence |
|---|---|---|---|
| Initial access | Reporting on a VPN-access advertisement for a pharmaceutical organisation | Demonstrates a market for pre-positioned access; listing authenticity remained unverified | Low |
| Malware delivery | Sekoia reporting on the rented Exvicy ClickFix framework | Monthly pricing and copied code illustrate commoditised delivery capability | Moderate |
| Infostealer data | Okta analysis of a multi-gigabyte dump containing sessions and API keys | Tokens and API keys can bypass password-centred controls | Moderate-High |
| Leaked data | A directly observed forum post claiming a retail database | Proves the advertisement existed, not that the breach occurred | Low |
| Cash-out infrastructure | Public crypto-fiat P2P group advertising escrow and zero fees | Confirms exchange infrastructure; does not prove criminal use or laundering | Low |

The main analytical lesson is that category membership is not equivalent to malicious proof. A P2P exchange, hosting service, or remote-access product can be legitimate while still being usable within a criminal workflow.

## Ransomware Ecosystem

### Qilin

Qilin is consistently described as an affiliate RaaS operation. Public reporting described tiered affiliate shares, while tracker data showed high posting activity during the collection snapshot. Access methods include exposed remote services and brokered credentials. A previously considered product-specific VPN attribution was removed because the captured evidence supported only the broader access pattern.

### SafePay

SafePay illustrates source conflict. One vendor page classified it as RaaS while the accompanying narrative described an internal operation without affiliates. News reporting also used the closed-team framing. The correct conclusion is a Moderate-confidence internal model, not certainty.

### Play

CISA describes Play as a presumed closed group and reports initial-access brokers tied to Play exploiting SimpleHelp. This supports a closed core with external access relationships, showing that "closed" does not mean fully self-contained.

| Group | Working model | Confidence |
|---|---|---|
| Qilin | Affiliate RaaS | High on model; Moderate on individual access claims |
| SafePay | Internal/closed operation | Moderate due source contradiction |
| Play | Presumed closed group using external access relationships | Moderate-High |

## Forum Culture Comparison

| Dimension | Russian-speaking ecosystem | English-speaking ecosystem |
|---|---|---|
| Access | Paid entry, deposits, reputation gates | More public surfaces and easier discovery |
| Governance | Complaints, arbitration, guarantors and cross-forum bans | Lighter reputation systems and repeated disruption |
| Specialisation | Access, exploits, malware and B2B services | Strong representation of leaked data, logs and accounts |
| Trust | Deposits and escrow reduce counterparty risk | Join date, post count, reputation and bans provide lighter signals |
| Resilience | Gated communities but repeated law-enforcement pressure | Successor forums and messaging channels absorb displaced users |

These are directional differences, not universal rules. The English-language evidence base was thinner and more directly observed; the Russian-language evidence was broader but relied more heavily on academic and vendor reporting.

## Intelligence Judgments

1. **Session tokens and API keys are increasingly valuable resale material - Moderate confidence.** Defenders should shorten token lifetime, scope API keys, and detect reuse from new locations.
2. **Delivery frameworks are commoditising - Low confidence.** One rented framework cannot establish a market-wide trend; behaviour-based detection is more durable than family naming.
3. **Valid accounts and exposed remote access remain central - Moderate confidence.** Phishing-resistant MFA, edge-system patching, and stealer-data monitoring directly raise attacker cost.
4. **Affiliate and closed ransomware models coexist - Moderate confidence.** Affiliate programmes may produce more variable tradecraft, while closed teams can create repeatable patterns.
5. **Public P2P and escrow services are not proof of laundering - Low confidence.** Monitor mule and rapid pass-through behaviour without treating group membership as criminal evidence.

## Evidence Quality

The underlying research log contained 52 entries, all reconciled to evidence. Source grading used:

- **Primary:** directly observed public page
- **Primary/archived:** actor material preserved by a tracker
- **Secondary:** government, vendor, academic, news, or tracker analysis

Primary observation means the page was seen. It does not validate the advertised breach, access, product, or transaction.

Selected public excerpts and the private integrity IDs are documented in the [case evidence index](../../evidence/case-01-underground-threat-economy.md).

## Defensive Takeaways

- Prioritise identity material and exposed access paths over marketplace branding.
- Treat ransomware leak-site volume as an activity signal, not market share.
- Require independent corroboration before operationalising marketplace claims.
- Preserve source lineage so repeated reporting is not mistaken for multiple sources.
- Record negative findings and collection limitations alongside positive hits.

## Skills Demonstrated

Passive underground-economy research, evidence reconciliation, source grading, RaaS/IAB analysis, comparative ecosystem analysis, confidence calibration, IOC hygiene, and defender-focused intelligence writing.

## Selected Sources

CISA, Sekoia, Okta, Halcyon, CybelAngel, Fortinet FortiGuard, Cybernews, Dark Reading/KELA, CloudSEK, Flare, TraceX Labs, Security Affairs, HackRead, public tracker records, and directly observed public pages.

- [CISA/FBI/ASD: Play Ransomware](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Halcyon: Qilin threat-group profile](https://www.halcyon.ai/threat-group/qilin)
- [CybelAngel: Qilin tactics](https://cybelangel.com/blog/qilin-ransomware-tactics-attack/)
- [FortiGuard: SafePay threat-actor profile](https://fortiguard.fortinet.com/threat-actor/6331/safepay-ransomware)
- [Dark Reading/KELA: Initial-access pricing](https://www.darkreading.com/threat-intelligence/average-cost-to-buy-access-to-a-compromised-company-1-000)

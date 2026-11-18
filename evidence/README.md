# Public Evidence And Verification

The portfolio reports are supported by a larger private evidence pack. Publishing every original capture would redistribute raw forum material, third-party pages, possible personal data, and unnecessary actor infrastructure. This directory provides a safer verification layer.

## What Is Public

- Selected metadata-free source excerpts
- Source names, URLs, publication and collection dates
- A statement of what each item supports and what it cannot prove
- SHA-256 hashes for selected private originals
- Reproducible passive-collection tools

## Evidence Indexes

| Case study | Public verification |
|---|---|
| Underground Threat Economy | [Evidence index](case-01-underground-threat-economy.md) |
| Exploit-Claim Credibility | [Evidence index](case-02-exploit-claim-credibility.md) |
| Handala Threat Actor | [Evidence index](case-03-handala-threat-actor.md) |
| Brand Exposure Monitoring | [Evidence index](case-04-brand-exposure-monitoring.md) |

The [private evidence manifest](PRIVATE-EVIDENCE-MANIFEST.md) records integrity hashes without exposing the original content.

## How Verification Works

To verify a privately supplied original on Windows:

```powershell
Get-FileHash -Algorithm SHA256 "path\to\evidence.png"
```

The result should match the corresponding manifest value exactly.

## Important Limits

- A hash proves that a later file matches the recorded file; it does not independently prove when the original was created.
- A screenshot proves that visible content existed when captured; it does not validate an actor, breach, exploit, or seller claim.
- Public excerpts remain third-party material and are included only for research commentary and verification.
- The complete private evidence pack may be demonstrated in a controlled review but is not appropriate for unrestricted publication.

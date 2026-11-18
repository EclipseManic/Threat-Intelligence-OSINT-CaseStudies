# Safe Passive-OSINT Tools

The DNS and defanging utilities use Python's standard library and perform no authentication, exploitation, form submission, or candidate-site content retrieval. The PDF builder additionally uses PyMuPDF for metadata and bookmarks.

Install the PDF-builder dependency:

```powershell
python -m pip install -r tools/requirements.txt
```

## DNS/PTR Snapshot

```powershell
python tools/passive_dns_snapshot.py example.com example.net
python tools/passive_dns_snapshot.py --file domains.txt --json
```

The tool records the UTC collection time, current IPv4 answers, and PTR names. Results are infrastructure metadata only and do not establish ownership or malicious intent.

## Defang

```powershell
python tools/defang.py https://example.com/path 192.0.2.10
```

## Build PDFs

```powershell
python tools/build_portfolio.py
```

The builder renders the four canonical Markdown case studies into `pdf/`. Microsoft Edge or Google Chrome is required.

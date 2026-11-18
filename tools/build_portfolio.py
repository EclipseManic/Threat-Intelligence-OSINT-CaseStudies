"""Render the public Markdown case studies as TLP:CLEAR PDFs."""

import html
import os
from pathlib import Path
import re
import shutil
import subprocess

import fitz


ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / ".build"
OUTPUT = ROOT / "pdf"


def browser_path():
    configured = os.environ.get("BROWSER")
    candidates = [
        configured,
        shutil.which("msedge"),
        shutil.which("chrome"),
        shutil.which("google-chrome"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return Path(candidate)
    raise FileNotFoundError("Microsoft Edge or Google Chrome was not found")


def inline(text):
    text = html.escape(text.replace(r"\|", "|"))
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def split_row(line):
    cells = []
    buffer = ""
    escaped = False
    for character in line.strip().strip("|"):
        if escaped:
            buffer += character
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == "|":
            cells.append(buffer.strip())
            buffer = ""
        else:
            buffer += character
    cells.append(buffer.strip())
    return cells


def is_separator(line):
    return bool(re.fullmatch(r"\|?[\s:\-|]+\|?", line.strip())) and "-" in line


def markdown_body(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    output = []
    index = 0
    list_type = None

    def close_list():
        nonlocal list_type
        if list_type:
            output.append(f"</{list_type}>")
            list_type = None

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped or re.fullmatch(r"-{3,}|\*{3,}", stripped):
            close_list()
            index += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading:
            close_list()
            level = min(len(heading.group(1)), 3)
            output.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        if stripped.startswith("|"):
            close_list()
            block = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                block.append(lines[index])
                index += 1
            rows = [split_row(row) for row in block if not is_separator(row)]
            if rows:
                output.append("<table><thead><tr>")
                output.extend(f"<th>{inline(cell)}</th>" for cell in rows[0])
                output.append("</tr></thead><tbody>")
                for row in rows[1:]:
                    output.append("<tr>")
                    output.extend(f"<td>{inline(cell)}</td>" for cell in row)
                    output.append("</tr>")
                output.append("</tbody></table>")
            continue

        if stripped.startswith(">"):
            close_list()
            output.append(f"<blockquote>{inline(stripped.lstrip('> ').strip())}</blockquote>")
            index += 1
            continue

        bullet = re.match(r"^[-*]\s+(.*)$", stripped)
        numbered = re.match(r"^\d+\.\s+(.*)$", stripped)
        if bullet or numbered:
            wanted = "ul" if bullet else "ol"
            if list_type != wanted:
                close_list()
                output.append(f"<{wanted}>")
                list_type = wanted
            output.append(f"<li>{inline((bullet or numbered).group(1))}</li>")
            index += 1
            continue

        close_list()
        output.append(f"<p>{inline(stripped)}</p>")
        index += 1

    close_list()
    return "\n".join(output)


def plain_heading(value):
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"\*([^*]+)\*", r"\1", value)
    return value.strip()


def headings(path):
    result = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,3})\s+(.*)$", line.strip())
        if match:
            result.append((len(match.group(1)), plain_heading(match.group(2))))
    return result


CSS = """
@page {
  size: A4;
  margin: 14mm 16mm 20mm;
  @bottom-center {
    content: "Manichand Gupta  |  Public Portfolio Case Study  |  TLP:CLEAR";
    color: #555;
    font-family: Arial, sans-serif;
    font-size: 7.5pt;
  }
}
* { box-sizing: border-box; }
body { margin: 0; color: #17212b; font-family: Arial, sans-serif; font-size: 9.4pt; line-height: 1.24; }
h1 { color: #163a5f; font-size: 20pt; margin: 0 0 8pt; }
h2 { color: #163a5f; font-size: 13.5pt; margin: 11pt 0 4pt; border-bottom: 0.5pt solid #b9c6d2; padding-bottom: 2pt; }
h3 { color: #24577f; font-size: 10.5pt; margin: 8pt 0 3pt; }
h1, h2, h3 { break-after: avoid; }
p { margin: 0 0 5pt; }
blockquote { margin: 4pt 0 7pt; padding: 5pt 7pt; border-left: 3pt solid #163a5f; background: #eef3f7; font-weight: 700; }
ul, ol { margin: 2pt 0 5pt 18pt; padding: 0; }
li { margin: 0 0 2pt; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; margin: 4pt 0 7pt; font-size: 7.9pt; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: #163a5f; color: white; font-weight: 700; }
th, td { border: 0.5pt solid #aeb9c3; padding: 3pt; vertical-align: top; overflow-wrap: anywhere; }
tbody tr:nth-child(even) { background: #f2f5f8; }
code { font-family: Consolas, monospace; font-size: 0.92em; }
a { color: #24577f; text-decoration: none; }
"""


def render(source, destination, title, browser):
    document = (
        "<!doctype html><html><head><meta charset='utf-8'><title>"
        + html.escape(title)
        + "</title><meta name='author' content='Manichand Gupta'><style>"
        + CSS
        + "</style></head><body>"
        + markdown_body(source)
        + "</body></html>"
    )
    html_path = BUILD / f"{destination.stem}.html"
    html_path.write_text(document, encoding="utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    profile = BUILD / "browser-profile"
    result = subprocess.run(
        [
            str(browser),
            "--headless",
            "--disable-gpu",
            "--disable-extensions",
            "--no-pdf-header-footer",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={destination}",
            html_path.as_uri(),
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"Failed to render {title}")

    pdf = fitz.open(destination)
    metadata = pdf.metadata
    metadata.update(
        {
            "title": title,
            "author": "Manichand Gupta",
            "subject": "Public threat-intelligence and OSINT portfolio case study",
            "keywords": "OSINT, threat intelligence, TLP:CLEAR, portfolio",
        }
    )
    pdf.set_metadata(metadata)
    toc = []
    start_page = 0
    for level, heading in headings(source):
        found = None
        for page_number in range(start_page, len(pdf)):
            if pdf[page_number].search_for(heading):
                found = page_number
                break
        if found is not None:
            toc.append([level, heading, found + 1])
            start_page = found
    if toc:
        pdf.set_toc(toc)
    processed = BUILD / f"{destination.stem}.processed.pdf"
    pdf.save(processed, garbage=4, deflate=True, clean=True)
    pdf.close()
    shutil.move(processed, destination)
    print(f"OK  {destination.relative_to(ROOT)}  ({destination.stat().st_size:,} bytes)")


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    browser = browser_path()
    jobs = [
        ("01-underground-threat-economy", "01 - Underground Threat Economy"),
        ("02-exploit-claim-credibility", "02 - Exploit Claim Credibility"),
        ("03-handala-threat-actor", "03 - Handala Threat Actor"),
        ("04-brand-exposure-monitoring", "04 - Brand Exposure Monitoring"),
    ]
    for directory, title in jobs:
        render(
            ROOT / "case-studies" / directory / "README.md",
            OUTPUT / f"{title}.pdf",
            title,
            browser,
        )
    shutil.rmtree(BUILD, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

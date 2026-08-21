"""Lightweight structural checks for the generated-free static site."""

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / name for name in ("index.html", "services.html", "thermographic-imaging.html", "about.html", "contact.html")]


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.titles, self.descriptions, self.canonicals, self.h1 = [], [], [], [], 0
        self.jsonld, self._script_type, self._script_text = [], None, []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "h1": self.h1 += 1
        if tag == "title": self.titles.append(True)
        if tag == "meta" and values.get("name") == "description": self.descriptions.append(values.get("content", ""))
        if tag == "link" and values.get("rel") == "canonical": self.canonicals.append(values.get("href", ""))
        for key in ("href", "src", "srcset"):
            if key in values: self.refs.append(values[key])
        if tag == "script":
            self._script_type = values.get("type")
            self._script_text = []

    def handle_data(self, data):
        if self._script_type == "application/ld+json": self._script_text.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._script_type == "application/ld+json":
            self.jsonld.append("".join(self._script_text))
        if tag == "script": self._script_type, self._script_text = None, []


def local_path(reference):
    reference = reference.split()[0].split("#")[0].split("?")[0]
    parsed = urlparse(reference)
    if parsed.scheme or reference.startswith(("mailto:", "tel:")): return None
    path = parsed.path
    if path == "/": return ROOT / "index.html"
    return ROOT / path.lstrip("/")


errors, titles, descriptions = [], set(), set()
for page in PAGES:
    parser = AuditParser(); parser.feed(page.read_text(encoding="utf-8"))
    if len(parser.titles) != 1: errors.append(f"{page.name}: expected one title")
    if len(parser.descriptions) != 1: errors.append(f"{page.name}: expected one meta description")
    if len(parser.canonicals) != 1: errors.append(f"{page.name}: expected one canonical")
    if parser.h1 != 1: errors.append(f"{page.name}: expected one h1, found {parser.h1}")
    for block in parser.jsonld:
        try: json.loads(block)
        except json.JSONDecodeError as exc: errors.append(f"{page.name}: invalid JSON-LD: {exc}")
    for ref in parser.refs:
        for part in ref.split(","):
            candidate = local_path(part.strip())
            if candidate and not candidate.exists(): errors.append(f"{page.name}: missing {candidate.relative_to(ROOT)}")
    if parser.descriptions and parser.descriptions[0] in descriptions: errors.append(f"{page.name}: duplicate meta description")
    descriptions.update(parser.descriptions)
    title_match = re.search(r"<title>(.*?)</title>", page.read_text(encoding="utf-8"), re.I | re.S)
    if title_match:
        title = title_match.group(1)
        if title in titles: errors.append(f"{page.name}: duplicate title")
        titles.add(title)

ET.parse(ROOT / "sitemap.xml")
identity = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
if identity["productionDomainVerified"] is not False: errors.append("Placeholder origin must remain explicitly unverified")
all_html = "\n".join(page.read_text(encoding="utf-8") for page in PAGES)
for forbidden in ("24/7", "emergency service", "years in business", "warranty", "guaranteed"):
    if forbidden.casefold() in all_html.casefold(): errors.append(f"Unverified claim found: {forbidden}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated {len(PAGES)} pages: metadata, headings, local references, JSON-LD, XML, and claim guardrails.")

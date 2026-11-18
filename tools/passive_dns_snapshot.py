"""Create a timestamped passive DNS and PTR snapshot."""

from argparse import ArgumentParser
from datetime import datetime, timezone
import json
from pathlib import Path
import socket


def ipv4_addresses(domain):
    try:
        return sorted(set(socket.gethostbyname_ex(domain)[2]))
    except OSError:
        return []


def reverse_name(address):
    try:
        return socket.gethostbyaddr(address)[0]
    except OSError:
        return None


def load_domains(arguments):
    domains = list(arguments.domains)
    if arguments.file:
        for line in Path(arguments.file).read_text(encoding="utf-8").splitlines():
            value = line.strip().lower()
            if value and not value.startswith("#"):
                domains.append(value)
    return sorted(set(domains))


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("domains", nargs="*", help="Domain names to resolve")
    parser.add_argument("--file", help="UTF-8 file containing one domain per line")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a table")
    arguments = parser.parse_args()
    domains = load_domains(arguments)
    if not domains:
        parser.error("provide at least one domain or --file")

    collected = datetime.now(timezone.utc).isoformat(timespec="seconds")
    records = []
    for domain in domains:
        addresses = ipv4_addresses(domain)
        records.append(
            {
                "domain": domain,
                "addresses": [
                    {"ipv4": address, "ptr": reverse_name(address)}
                    for address in addresses
                ],
            }
        )

    if arguments.json:
        print(json.dumps({"collected_utc": collected, "records": records}, indent=2))
        return 0

    print(f"Collected UTC: {collected}")
    print("DNS/PTR queries only; no HTTP requests\n")
    print(f"{'domain':32} {'ipv4':16} ptr")
    print("-" * 100)
    for record in records:
        if not record["addresses"]:
            print(f"{record['domain']:32} {'-':16} not resolved")
            continue
        for address in record["addresses"]:
            print(
                f"{record['domain']:32} {address['ipv4']:16} "
                f"{address['ptr'] or '(no PTR)'}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Defang URLs, domains, and IP addresses for intelligence reporting."""

from argparse import ArgumentParser
import re


def defang(value):
    value = re.sub(r"^https://", "hxxps://", value, flags=re.IGNORECASE)
    value = re.sub(r"^http://", "hxxp://", value, flags=re.IGNORECASE)
    return value.replace(".", "[.]")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("values", nargs="+", help="Values to defang")
    arguments = parser.parse_args()
    for value in arguments.values:
        print(defang(value))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

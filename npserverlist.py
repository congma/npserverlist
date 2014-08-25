#!/usr/bin/env python
"""npserverlist.py -- get NTP pool server list by zone.

USAGE:
    npserverlist.py zone-name

EXIT CODE:
    0:  The program exits successfully.
    1:  Error retrieving server list from ntp.org website.
    2:  Invalid input.
"""


import sys
import re
import urllib2


CONT_ZONES = frozenset(("africa", "asia", "europe",
                  "north-america", "oceania", "south-america"))
RE_MATCH = re.compile(r"^server\s+[0-9a-z\-\.]+\.pool\.ntp\.org$")


def makeurl(zone):
    """Returns URL for given zone."""
    return "http://www.pool.ntp.org/zone/%s" % zone


def zone_by_name(text):
    """Returns possible zone-name by given input string.  If not possibly a
    valid zone-name, return None."""
    name = text.strip().lower()
    if name in CONT_ZONES:
        return name
    if name.isalpha() and len(name) == 2:
        return name
    return None


def scrape(doc):
    """Generator yielding scraping results."""
    s_inpre = False
    s_matched = False
    for line in doc:
        clean_line = line.strip()
        if clean_line.lower() == "<pre>":
            s_inpre = True
            continue
        if s_inpre:
            match = RE_MATCH.match(clean_line)
            if match:
                s_matched = True
                yield match.group()
                continue
        if s_matched and clean_line.lower() == "</pre>":
            break


def show_usage():
    """Displays usage."""
    print >> sys.stderr, "Usage: %s zone-name" % sys.argv[0]


def main():
    """Main routine."""
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(2)
    zone = zone_by_name(sys.argv[1])
    if zone is None:
        print >> sys.stderr, ("Error: Zone name not understood: %s" %
                              sys.argv[1])
        sys.exit(2)
    url = makeurl(zone)
    try:
        req = urllib2.urlopen(url)
    except urllib2.URLError as urle:
        print >> sys.stderr, ("Error: Failed to retrieve configuration: %s" %
                              urle.reason)
        sys.exit(1)
    lines = req.readlines()
    req.close()
    resgen = scrape(lines)
    for res in resgen:
        print res
    sys.exit(0)


if __name__ == "__main__":
    main()

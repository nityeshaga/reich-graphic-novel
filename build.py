#!/usr/bin/env python3
"""Generate pages.json manifest from output/ PNGs for the reader."""

import json
import os
import re

OUTPUT_DIR = "output"

# Only need to define where part/chapter headers appear (by page number).
# Titles and subtitles are derived from filenames automatically.
PART_HEADERS = {
    0: "PROLOGUE",
    1: "PART I — THE LANGUAGE OF LIFE",
    6: "CHAPTER 2 — HOW LIFE COPIES ITSELF",
    10: "CHAPTER 3 — THREE HISTORIES IN YOUR BODY",
    14: "CHAPTER 4 — READING THE DEAD",
    18: "EPILOGUE",
}

UPCOMING = [
    {"part": "PART II — THE DEEP PAST", "chapters": [
        "Chapter 5: The Family We Forgot",
        "Chapter 6: The Braided River",
        "Chapter 7: Africa's Own Story",
    ]},
    {"part": "PART III — THE WORLD REMADE", "chapters": [
        "Chapter 8: The Three Peoples of Europe",
        "Chapter 9: The Horsemen and the Plague",
        "Chapter 10: The Collision That Formed India",
    ]},
    {"part": "PART IV — THE WIDER WORLD", "chapters": [
        "Chapter 11: The First Americans",
        "Chapter 12: The Genomic Origins of East Asia",
        "Chapter 13: The Pacific Voyagers",
    ]},
    {"part": "PART V — WHAT IT ALL MEANS", "chapters": [
        "Chapter 14: Power and Sex",
        "Chapter 15: The Race Question",
        "Chapter 16: The Voice in the DNA",
        "Chapter 17: The Lost Civilizations Question",
        "Chapter 18: The Grand Challenge",
        "Chapter 19: What This Means for AI",
    ]},
]


def slug_to_title(slug):
    """Convert 'the-copy-machine' to 'The Copy Machine'."""
    return slug.replace("-", " ").title()


def main():
    pattern = re.compile(r"^page-(\d+)-(.+)\.png$")
    pages = []

    for f in sorted(os.listdir(OUTPUT_DIR)):
        m = pattern.match(f)
        if not m:
            continue
        if re.search(r"-v\d+\.png$", f):
            continue
        num = int(m.group(1))
        slug = m.group(2)
        entry = {
            "file": f"output/{f}",
            "title": slug_to_title(slug),
        }
        if num in PART_HEADERS:
            entry["part"] = PART_HEADERS[num]
        pages.append(entry)

    manifest = {"pages": pages, "upcoming": UPCOMING}
    with open("pages.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Generated pages.json with {len(pages)} pages")


if __name__ == "__main__":
    main()

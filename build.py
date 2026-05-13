#!/usr/bin/env python3
"""Generate pages.json manifest from output/ PNGs for the reader."""

import json
import os
import re

OUTPUT_DIR = "output"

# Part headers keyed by page number (index in the sorted page list)
PART_HEADERS = {
    0: "PROLOGUE",
    1: "PART I — THE LANGUAGE OF LIFE",
    19: "PART II — THE DEEP PAST",
    20: "PART III — THE WORLD REMADE",
    21: "PART IV — THE WIDER WORLD",
    22: "PART V — WHAT IT ALL MEANS",
    23: "EPILOGUE",
}

# Chapter assignments keyed by page number (index in sorted page list)
# v4 storyboard: Ch1 = 5 pages (The Molecule), remaining v3 pages still present
CHAPTERS = {
    1: "Part I Intro",
    2: "Chapter 1: The Molecule",
    3: "Chapter 1: The Molecule",
    4: "Chapter 1: The Molecule",
    5: "Chapter 1: The Molecule",
    6: "Chapter 1: The Molecule",
    7: "Chapter 4: How Life Copies Itself",
    8: "Chapter 4: How Life Copies Itself",
    9: "Chapter 4: How Life Copies Itself",
    10: "Chapter 4: How Life Copies Itself",
    11: "Chapter 5: Three Histories in Your Body",
    12: "Chapter 5: Three Histories in Your Body",
    13: "Chapter 5: Three Histories in Your Body",
    14: "Chapter 5: Three Histories in Your Body",
    15: "Chapter 6: Reading the Dead",
    16: "Chapter 6: Reading the Dead",
    17: "Chapter 6: Reading the Dead",
    18: "Chapter 6: Reading the Dead",
    19: "Part II Intro",
    20: "Part III Intro",
    21: "Part IV Intro",
    22: "Part V Intro",
    23: "Epilogue Intro",
    24: "Chapter 22: Back to the Headphones",
    25: "Chapter 22: Back to the Headphones",
}

UPCOMING = [
    {"part": "PART I — THE LANGUAGE OF LIFE (remaining)", "chapters": [
        "Chapter 2: Your Parents' Gift",
        "Chapter 3: When the Code Changes",
    ]},
    {"part": "PART II — THE DEEP PAST", "chapters": [
        "Chapter 7: The Family We Forgot",
        "Chapter 8: The Braided River",
        "Chapter 9: Africa's Own Story",
    ]},
    {"part": "PART III — THE WORLD REMADE", "chapters": [
        "Chapter 10: The Three Peoples of Europe",
        "Chapter 11: The Horsemen and the Plague",
        "Chapter 12: The Collision That Formed India",
    ]},
    {"part": "PART IV — THE WIDER WORLD", "chapters": [
        "Chapter 13: The First Americans",
        "Chapter 14: The Genomic Origins of East Asia",
        "Chapter 15: The Pacific Voyagers",
    ]},
    {"part": "PART V — WHAT IT ALL MEANS", "chapters": [
        "Chapter 16: Power and Sex",
        "Chapter 17: The Race Question",
        "Chapter 18: The Voice in the DNA",
        "Chapter 19: The Lost Civilizations Question",
        "Chapter 20: The Grand Challenge",
        "Chapter 21: What This Means for AI",
    ]},
]


TITLE_OVERRIDES = {
    "intro-part1": "The Journey Ahead",
    "intro-part2": "You Have the Language",
    "intro-part3": "The River Has Names",
    "intro-part4": "The Pattern Repeats",
    "intro-part5": "Now Ask Why",
    "intro-epilogue": "The Full Map",
}


def slug_to_title(slug):
    """Convert 'the-copy-machine' to 'The Copy Machine'."""
    if slug in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[slug]
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
        slug = m.group(2)
        entry = {
            "file": f"output/{f}",
            "title": slug_to_title(slug),
        }
        idx = len(pages)
        if idx in PART_HEADERS:
            entry["part"] = PART_HEADERS[idx]
        if idx in CHAPTERS:
            entry["chapter"] = CHAPTERS[idx]
        pages.append(entry)

    manifest = {"pages": pages, "upcoming": UPCOMING}
    with open("pages.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Generated pages.json with {len(pages)} pages")


if __name__ == "__main__":
    main()

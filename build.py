#!/usr/bin/env python3
"""Generate pages.json manifest from output/ PNGs for the reader."""

import json
import os
import re

OUTPUT_DIR = "output"

# Map page keys to metadata. Keys are strings to support "3b" style pages.
PAGE_META = {
    "0": ("Prologue", "I couldn't follow the podcast", "PROLOGUE"),
    "1": ("Ch 1 — The Molecule", "What's Written Inside You", "PART I — THE LANGUAGE OF LIFE"),
    "2": ("Ch 1 — The Central Dogma", "DNA → RNA → Protein", None),
    "3": ("Ch 1 — Inheritance", "How You Got Your Genes", None),
    "3b": ("Ch 1 — Beyond the Pea Plants", "Codominance, Polygenic Traits, Sex-Linked", None),
    "4": ("Ch 1 — Mutations", "When the Code Changes", None),
    "5": ("Ch 2 — The Copy Machine", "DNA Replication", "CHAPTER 2 — HOW LIFE COPIES ITSELF"),
    "6": ("Ch 2 — Two Ways to Divide", "Mitosis vs Meiosis", None),
    "7": ("Ch 2 — Recombination", "The Key to History", None),
    "8": ("Ch 2 — The Rebels", "The Rebels That Don't Shuffle", None),
    "9": ("Ch 3 — The Big Record", "Nuclear DNA", "CHAPTER 3 — THREE HISTORIES IN YOUR BODY"),
    "10": ("Ch 3 — The Mother Line", "Mitochondrial DNA", None),
    "11": ("Ch 3 — The Father Line", "Y Chromosome", None),
    "12": ("Ch 3 — When the Stories Disagree", "The Central Mystery", None),
    "13": ("Ch 4 — The Clean Room", "Reading the Dead", "CHAPTER 4 — READING THE DEAD"),
    "14": ("Ch 4 — Sequencing", "Sequencing and Comparing", None),
    "15": ("Ch 4 — The Finger Bone", "The Finger Bone That Changed Everything", None),
    "16": ("Ch 4 — The Cast Assembles", "The Human Family Portrait", None),
    "17": ("Ch 5 — Not Dumb Cavemen", "Neanderthal Rehabilitation", "PART II — THE DEEP PAST"),
    "18": ("Ch 5 — The Encounter", "When We Met Neanderthals", None),
    "19": ("Ch 5 — The Purge", "Purifying Selection", None),
    "20": ("Ch 5 — Are We Even Modern?", "The 2% vs 10-20% Bombshell", None),
    "21": ("Ch 6 — The Archipelago", "50,000 Years Ago", "CHAPTER 6 — THE BRAIDED RIVER"),
    "22": ("Ch 6 — The Spark", "The Forest Fire Metaphor", None),
    "23": ("Ch 6 — Not Out of Africa", "Within Everything", None),
    "24": ("Ch 6 — The Trellis", "Not the Tree", None),
    "25": ("Ch 7 — We Left Africa", "Africa's Neglected History", "CHAPTER 7 — AFRICA'S OWN STORY"),
    "26": ("Ch 7 — The Deep Mixture", "The Mixture That Made Us", None),
    "27": ("Ch 7 — The Bantu Expansion", "Three Sickle Cells", None),
    "28": ("Ch 7 — Tessellated Past", "Africa's Genetic Landscape", None),
    "29": ("Ch 8 — The Layer Cake", "Three Peoples of Europe", "PART III — THE WORLD REMADE"),
    "30": ("Ch 8 — The Iceman", "Ötzi's Closest Relatives", None),
    "31": ("Ch 8 — The Farmers Arrive", "9,000 Years Ago", None),
    "32": ("Ch 8 — The Ghost Beneath", "Basal Eurasians", None),
    "33": ("Ch 9 — The Yamnaya", "Horsemen of the Steppe", "CHAPTER 9 — THE HORSEMEN AND THE PLAGUE"),
    "34": ("Ch 9 — 90% Gone", "Population Replacement", None),
    "35": ("Ch 9 — What Cleared the Way", "Yersinia Pestis", None),
    "36": ("Ch 9 — The Relay Race", "Sex-Biased Migration", None),
    "37": ("Ch 10 — Two Ghosts", "ANI and ASI", "CHAPTER 10 — THE COLLISION THAT FORMED INDIA"),
    "38": ("Ch 10 — The Rig Veda", "Rig Veda as Evidence", None),
    "39": ("Ch 10 — 3,000 Years of Silence", "The Vysya", None),
    "40": ("Ch 10 — The Diwali Negotiation", "Science vs Politics", None),
    "41": ("Ch 11 — Not Clovis First", "The First Americans", "PART IV — THE WIDER WORLD"),
    "42": ("Ch 11 — Population Y", "The Amazonian Mystery", None),
    "43": ("Ch 11 — Kennewick Man", "Ancient DNA Settles It", None),
    "44": ("Ch 11 — Greenberg Was Right", "Linguistics Meets Genetics", None),
    "45": ("Ch 12 — Two Rivers", "Yellow River and Yangtze", "CHAPTER 12 — GENOMIC ORIGINS OF EAST ASIA"),
    "46": ("Ch 12 — Taiwan to Madagascar", "The Austronesian Expansion", None),
    "47": ("Ch 12 — The Japanese Melting Pot", "80% Farmer, 20% Hunter", None),
    "48": ("Ch 12 — The Blitzkrieg", "5,000 Years of Expansion", None),
    "49": ("Ch 13 — The Empty Ocean", "Pacific Voyagers", "CHAPTER 13 — THE PACIFIC VOYAGERS"),
    "50": ("Ch 13 — The Reversal", "Papuan Males Arrive", None),
    "51": ("Ch 13 — The Surprise of Sex", "Inverted Expectations", None),
    "52": ("Ch 13 — Huxley's Line", "Biogeography and Genetics", None),
    "53": ("Ch 14 — Y-Chromosome Collapse", "Power and Sex", "PART V — WHAT IT ALL MEANS"),
    "54": ("Ch 14 — Written in Bone", "Yamnaya Kurgans", None),
    "55": ("Ch 14 — The Scars", "Genetic Scars of Slavery", None),
    "56": ("Ch 14 — The Pattern", "DNA Records What We Did", None),
    "57": ("Ch 15 — Both Sides Are Wrong", "The Race Question", "CHAPTER 15 — THE RACE QUESTION"),
    "58": ("Ch 15 — What Selection Changed", "10,000 Years of Adaptation", None),
    "59": ("Ch 15 — Watson and Wade", "Premature Conclusions", None),
    "60": ("Ch 15 — The Responsibility", "Filling the Vacuum", None),
    "61": ("Ch 16 — Beyond the Letters", "Epigenetics", "CHAPTER 16 — THE VOICE IN THE DNA"),
    "62": ("Ch 16 — The Vocal Tract", "The Revolution", None),
    "63": ("Ch 16 — Language", "Language and the Revolution", None),
    "64": ("Ch 16 — What We Don't Know", "Humility Before Data", None),
    "65": ("Ch 17 — Parallel Invention", "Lost Civilizations", "CHAPTER 17 — THE LOST CIVILIZATIONS QUESTION"),
    "66": ("Ch 17 — What Would We See", "Evidence of Early Civilization", None),
    "67": ("Ch 17 — Why Not?", "Why Did It Take So Long?", None),
    "68": ("Ch 17 — The Humbling", "We Keep Being Wrong", None),
    "69": ("Ch 18 — The Africa Problem", "The Grand Challenge", "CHAPTER 18 — THE GRAND CHALLENGE"),
    "70": ("Ch 18 — The Ancient DNA Atlas", "Reich's Vision", None),
    "71": ("Ch 18 — The Rabbi's Counsel", "Ethics of Ancient DNA", None),
    "72": ("Ch 18 — Mixtures All the Way Down", "The Final Thesis", None),
    "73": ("Ch 19 — The Scaling Argument", "AI and Evolution", "CHAPTER 19 — WHAT THIS MEANS FOR AI"),
    "74": ("Ch 19 — The 3x Problem", "Brains vs Compute", None),
    "75": ("Ch 19 — The Cultural Ratchet", "Connected Is Better", None),
    "76": ("Ch 19 — The Honest Answer", "Humility About Predictions", None),
    "77": ("Epilogue — The Return", "Back to the Headphones", "EPILOGUE"),
    "78": ("Epilogue — Helix's Goodbye", "You Were Never Just One Thing", None),
}

UPCOMING_CHAPTERS = [
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

def sort_key(key):
    """Sort keys like '0', '1', '3', '3b', '4', '77' naturally."""
    m = re.match(r"(\d+)(\D*)", key)
    return (int(m.group(1)), m.group(2))

def main():
    pattern = re.compile(r"^page-(\d+[a-z]?)-(.+)\.png$")
    raw_pages = []
    found_numbers = set()

    for f in sorted(os.listdir(OUTPUT_DIR)):
        m = pattern.match(f)
        if not m:
            continue
        if re.search(r"-v\d+\.png$", f):
            continue
        key = m.group(1).lstrip("0") or "0"
        found_numbers.add(int(re.match(r"\d+", key).group()))
        meta = PAGE_META.get(key, (f"Page {key}", "", None))
        entry = {
            "file": f"output/{f}",
            "title": meta[0],
            "subtitle": meta[1],
            "_key": key,
        }
        if meta[2]:
            entry["part"] = meta[2]
        raw_pages.append(entry)

    raw_pages.sort(key=lambda p: sort_key(p["_key"]))
    pages = [{k: v for k, v in p.items() if k != "_key"} for p in raw_pages]

    # figure out which upcoming chapters still don't have any pages
    upcoming = []
    chapter_page_ranges = {
        5: range(17, 21), 6: range(21, 25), 7: range(25, 29),
        8: range(29, 33), 9: range(33, 37), 10: range(37, 41),
        11: range(41, 45), 12: range(45, 49), 13: range(49, 53),
        14: range(53, 57), 15: range(57, 61), 16: range(61, 65),
        17: range(65, 69), 18: range(69, 73), 19: range(73, 77),
    }

    for section in UPCOMING_CHAPTERS:
        remaining_chapters = []
        for ch_label in section["chapters"]:
            ch_num = int(re.search(r"(\d+)", ch_label).group(1))
            page_range = chapter_page_ranges.get(ch_num, [])
            if not any(p in found_numbers for p in page_range):
                remaining_chapters.append(ch_label)
        if remaining_chapters:
            upcoming.append({"part": section["part"], "chapters": remaining_chapters})

    manifest = {"pages": pages, "upcoming": upcoming}
    with open("pages.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Generated pages.json with {len(pages)} pages, {sum(len(s['chapters']) for s in upcoming)} upcoming chapters")

if __name__ == "__main__":
    main()

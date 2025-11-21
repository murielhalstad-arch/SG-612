# heuristics.py
import re

LABEL_RULES = {
    "School": ["innlever", "foreles", "canvas", "oppgave", "eksamen", "studie"],
    "Work":   ["møte", "rapport", "kunde", "prosjekt", "budsjett", "send faktura"],
    "Home":   ["bleier", "mat", "rengjør", "vask", "butikk", "middag", "hage"],
}

PRIORITY_RULES = {
    5: ["i dag", "nå", "haster", "kritisk", "fristen går ut"],
    4: ["i morgen", "snarest", "urgent"],
    2: ["senere", "når tid", "low"],
}

def classify_label(text: str) -> str:
    t = text.lower()
    for label, kws in LABEL_RULES.items():
        if any(kw in t for kw in kws):
            return label
    return "Other"

def classify_priority(text: str) -> int:
    t = text.lower()
    for p, kws in PRIORITY_RULES.items():
        if any(kw in t for kw in kws):
            return p
    m = re.search(r"(prio|prioritet)\s*([1-5])", t)  # f.eks. "prio 4"
    if m:
        return int(m.group(2))
    return 3  # standard

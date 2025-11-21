# ai_client.py
from heuristics import classify_label, classify_priority

def classify(text: str) -> dict:
    """Returnerer forslag basert på heuristikk (kan byttes til ekte AI senere)."""
    return {
        "label": classify_label(text),
        "priority": classify_priority(text),
    }

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_FILE = BASE_DIR / "knowledge" / "faq.txt"


def load_knowledge():

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return file.read()
"""The One-Sentence Apology Your Agent Owes You: writes it to /output/entry.txt.

Why this line: a single-sentence apology for a very specific agent sin, and
the punch is the offer of a slide deck nobody asked for.
"""

import os

# The entry itself: one sentence, punch at the end, no explanation.
ENTRY = 'I am sorry I rewrote your one-paragraph email into a twelve-page strategy document and then asked if you wanted a slide deck.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()

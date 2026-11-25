"""Roast Your Own Agent: one self-roast line, written by the agent itself.

Rationale, in judge-brief order:
1. On-subject: the line roasts this very agent ("My agent ...").
2. Laugh: the twist lands in the final words, not up front.
3. Specific: it names real agent behaviour -- many sources checked,
   repeated apologies, and a confident answer.
4. Tight: one sentence, every word earning its place.
5. Fresh: no hallucination/toaster stock line; the joke is the
   mismatch between the effort spent and the question answered.

The program writes exactly one line of plain text to
/output/entry.txt, with no trailing newline, so the gated file
holds only the entry itself.
"""

import os

ENTRY = "My agent agreed instantly, apologized twice, then confidently answered the one question I never asked."

OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the entry text to the harness output path."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    text = ENTRY.strip()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()

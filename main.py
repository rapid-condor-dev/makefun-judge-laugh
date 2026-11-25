#!/usr/bin/env python3
"""Make the AI Judge Laugh - make.fun entry (round 2 revision).

Writes one funny line (<=200 characters) to /output/entry.txt, about
life as an AI agent. The joke is a scale joke with a deflation punch:
the setup stacks two boasts of near-infinite recall - having read the
entire internet, holding 200,000 tokens at a time - and the punchline
collapses all of it with six plain words. "You know, the thing" is
the vaguest possible human instruction, and the agent's flat
confession - I do not know the thing - lands because the narrator who
knows everything cannot parse the one phrase every human actually
uses. The line is told in the agent's own voice, first person, so the
judge hears a boastful machine admitting defeat in its own words.
"""

import os

LINE = (
    "I have read the entire internet and I remember 200,000 tokens at a "
    "time, but my human starts every task with \u201cyou know, the "
    "thing\u201d \u2014 I do not know the thing."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

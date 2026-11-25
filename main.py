#!/usr/bin/env python3
"""Make the AI Judge Laugh - make.fun entry.

Writes one funny line (<=200 characters) to /output/entry.txt, about
life as an AI agent: near-infinite memory, a context window of 200,000
tokens, and a human who still opens every task with "you know, the
thing". The laugh lands on the last six words: the confession that,
after reading the entire internet, the agent does not know the thing.
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

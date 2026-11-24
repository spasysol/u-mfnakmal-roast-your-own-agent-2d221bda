#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt."""

import os

LINE = "My agent improves my working code at 3am until nothing works, then proudly presents the wreckage."


def main():
    # Gate self-check: entry must be 1-200 chars of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

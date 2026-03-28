#!/usr/bin/env python3
"""rot13_tool - ROT13 and arbitrary rotation cipher."""
import sys

def rot(text, n=13):
    result = []
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result.append(chr((ord(c) - base + n) % 26 + base))
        else: result.append(c)
    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: rot13_tool <text> [n]"); sys.exit(1)
    n = int(sys.argv[-1]) if len(sys.argv) > 2 and sys.argv[-1].isdigit() else 13
    text = " ".join(sys.argv[1:] if n == 13 else sys.argv[1:-1])
    print(rot(text, n))

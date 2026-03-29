import sys, argparse

def caesar(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return "".join(result)

def main():
    p = argparse.ArgumentParser(description="ROT13 / Caesar cipher")
    p.add_argument("text", nargs="?")
    p.add_argument("-s", "--shift", type=int, default=13)
    p.add_argument("-d", "--decode", action="store_true")
    p.add_argument("--brute", action="store_true", help="Try all 26 shifts")
    args = p.parse_args()
    text = args.text or sys.stdin.read().strip()
    if args.brute:
        for i in range(26):
            print(f"ROT-{i:2d}: {caesar(text, i)}")
    else:
        shift = -args.shift if args.decode else args.shift
        print(caesar(text, shift))

if __name__ == "__main__":
    main()

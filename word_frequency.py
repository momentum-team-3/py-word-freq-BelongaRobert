STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(fname):
    counts = {}

    with open(fname) as infile:
        words = infile.read().lower().split()

    for word in words:
        filtered = []
        
        for c in word:
            if c.isalpha():
                filtered.append(c)

        new = "".join(filtered)

        if new not in STOP_WORDS:
            if new in counts:
                counts[new] = counts[new] + 1
            
            else:
                counts[new] = 1

    width = max([len(k) for k in counts])
    for k in counts:
        print(f"{k:>{width}} | {counts[k]} {'*' * counts[k]}")


if __name__ == "__main__":
    import sys

    try:
        filename = sys.argv[1]
        
        if "-v" in sys.argv:
            print(f"This is the value of sys.argv: {sys.argv}")
            print(f"This is the filename you gave as an argument: {filename}")

        print_word_freq(filename)

    except IndexError:
        print("usage: python3 word_frequency.py <filename>")
        exit(1)

    except FileNotFoundError:
        print(f"No file named {filename} exists!")
        exit(1)

    else:
        exit(0)
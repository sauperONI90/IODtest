import sys
from collections import Counter

def main():
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <filename>")
        return

    filename = sys.argv[1]

    N = int(input("Enter the number of most common words to display: "))

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.lower().split()
    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words[:N]:
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()

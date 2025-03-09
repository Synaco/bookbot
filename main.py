from stats import get_word_count
from stats import get_char_dict
from stats import get_char_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_word_count(text.split())
    char_dict = get_char_dict(" ".join(text))
    results = get_char_count(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in results:
        print(f"{dict["key"]}: {dict["value"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

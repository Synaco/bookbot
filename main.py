from stats import get_word_count
from stats import get_char_dict
from stats import get_char_count

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_word_count(text.split())
    char_dict = get_char_dict(text)
    #char_count_list = get_char_count(char_dict)
    print(f"{num_words} words found in the document")
    print(char_dict)
    #get_char_dict(text)
    #print(get_char_count(char_dict))


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

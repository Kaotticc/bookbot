import sys
from stats import *
if len(sys.argv) != 2:
    sys.exit("Usage: python3 main.py <path_to_book>")
book = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    text = get_book_text(book)
    word_count = get_book_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = get_letter_count(text)
    sorted = sort_dict(letter_count)
    for char in sorted:
        print(char["char"] + ": " + str(char["num"]))

main()
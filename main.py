def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count(book):
    with open(book) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        return len(word_list)


def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_book_word_count("./books/frankenstein.txt")
    print(f"Found {word_count} total words")

main()
def get_book_word_count(book):
    word_list = book.split()
    return len(word_list)

def get_letter_count(book):
    letter_count = {}
    for l in list(book.lower()):
        if l in letter_count:
            letter_count[l] += 1
        else: letter_count[l] = 1
    return(letter_count)

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    for entry in dict:
        if entry.isalpha():
            n = dict[entry]
            dict_list.append({"char": entry, "num": n})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list




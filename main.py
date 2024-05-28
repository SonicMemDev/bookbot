def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    wordcount = get_wordcount(text)
    char_dict = get_chars(text)
    report(book_path, wordcount, char_dict)


def report(book, wordcount, dict):
    sorted_list = sort_dict_to_list(dict)
    
    print(f"--- Begin report of {book} ---")
    print(f"{wordcount} words found in document")
    print("")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")
    
def sort_on(dict):
    return dict["num"]

def sort_dict_to_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_wordcount(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def get_chars(text):
    lowered = text.lower()
    char_dict = {}
    for c in lowered:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


main()
import sys
arguments=len(sys.argv)
if  arguments != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
    word_count, 
    character_count, 
    sorted_character_list,
)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    chars_sorted_list = sorted_character_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


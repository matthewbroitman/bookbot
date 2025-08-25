def get_book_text(filepath):
    file_contents=None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import character_count

def main():
    file_contents=get_book_text("books/frankenstein.txt")
    print (character_count(file_contents))

main()


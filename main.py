from stats import *
import sys


def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()
    

sys.argv  # Add the path to the command line arguments
print(sys.argv)


for arg in sys.argv:
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if arg == sys.argv[0]: #skip the first argument which is the name of the script
        continue
    
    path = arg
    book = get_book_text(path)
    num_words = get_num_words(book)
    dict_unique_letters = count_unique_letters(book)
    sorted_dict = sort_dict(dict_unique_letters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter, count in sorted_dict:
        if letter.isalpha():
            print(f"{letter}: {count}")
        else:
            continue
    print("============= END ===============")
    

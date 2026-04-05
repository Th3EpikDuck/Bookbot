import sys

from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
        
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # word count
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # character count
    char_count = get_char_count(text)
    sorted_chars = sort_chars(char_count)

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
    
main()

from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_num_words(text)
    print(f"Found {count} total words")
    char_count = get_char_count(text)
    print(char_count)
    sorted_chars = sort_chars(text)
    print(sorted_chars)
    
main()

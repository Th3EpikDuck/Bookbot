from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_num_words(text)
    print(f"Found {count} total words")

main()

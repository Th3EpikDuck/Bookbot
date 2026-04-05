def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def word_count(text):
    new_text = text.split()
    return len(new_text)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_count(text)
    print(f"Found {word_count} total words")

main()

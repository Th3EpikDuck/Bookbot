def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()

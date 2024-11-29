def get_book_text_by_path(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    text = get_book_text_by_path("books/frankenstein.txt")
    print(text)

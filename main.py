def get_book_text_by_path(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters_insensitive(text):
    text = text.lower()
    characters = dict()
    for char in text:
        if char not in characters:
            characters[char] = 1
        characters[char] += 1
    print(characters)


if __name__ == "__main__":
    text = get_book_text_by_path("books/frankenstein.txt")
    print("Number of words:")
    print(count_words(text))
    print("Counted characters:")
    print(count_characters_insensitive(text))

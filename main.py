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
            characters[char] = 0
        characters[char] += 1
    return characters


if __name__ == "__main__":
    text = get_book_text_by_path("books/frankenstein.txt")
    number_of_words = count_words(text)
    characters_dic = count_characters_insensitive(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for key in characters_dic:
        print(f"The '{key}' character was found {characters_dic[key]} times")
    print("--- End report ---")

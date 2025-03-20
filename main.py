def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = "books/frankenstein.txt"
   
    text = get_book_text(file_path)
    number = number_of_words(text)
    print(f"{number} words found in the document")

main()
from stats import number_of_words
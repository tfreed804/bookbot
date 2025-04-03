#import functions from stats.py
from stats import word_count
from stats import character_count

#This function will open the .txt file of a book and save its contents as a string
def get_book_text(file_path):
    with open(file_path) as book:
        book_text = book.read()

        return book_text

#This function prints the text of the book bring read    
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_count(text)
    num_chars = character_count(text)
    
    print(f"{num_words} words found in the document")
    print(character_count(text))


main()

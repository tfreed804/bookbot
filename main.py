#import functions from stats.py
from stats import word_count
from stats import character_count
from stats import final_report

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
    sorted_chars = final_report(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")


main()

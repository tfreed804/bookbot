#This function will provide a word count for the book that is being read    
def word_count(book_text):
    individual_words = book_text.split()
    return len(individual_words)

#This function will provide a count of how many times an individual character appears.
def character_count(book_text):
    book_text = book_text.lower()
    count_dict = {}

    for char in book_text:
        if char.isprintable():
            count_dict[char] = count_dict.get(char, 0) + 1
    
    return count_dict
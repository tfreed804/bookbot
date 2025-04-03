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

#This function will allow me to sort the new dictionary below
def sort_on(dict):
    return dict["count"]

#this function will create a list of dictionaries from the original count_dict dictionary
#in the character_count function.
def final_report(count_dict):
    list_of_dicts = [{"char": k, "count": v} for k, v in count_dict.items() if k.isalpha()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts
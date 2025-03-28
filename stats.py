full_path = "books/frankenstein.txt"

def get_book_text(full_path):
        with open(full_path) as f:
                file_contents = f.read()
        return file_contents

def main():

    file_contents = get_book_text(full_path)
    return file_contents

def seperate_words():

            file_contents = main()
            words_count = 0
            split_words = file_contents.split()
            for i in split_words:
                words_count += 1
            print(f"{words_count} words found in the document") 

seperate_words()

def character_counter():

    counter = {}
    file_list = get_book_text(full_path)
    lower_list = file_list.lower()
    
    for character in lower_list:
        if character not in counter:
            counter[character] = 1 
        else: 
            counter[character] += 1
            
    print(counter)

character_counter()

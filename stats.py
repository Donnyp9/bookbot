import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

full_path = sys.argv[1]

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
            print(f"Found {words_count} total words") 


def character_counter():

    counter = {}
    file_list = get_book_text(full_path)
    lower_list = file_list.lower()
    
    for character in lower_list:
        if character not in counter:
            counter[character] = 1 
        else: 
            counter[character] += 1
            
    return counter


def sorter(counter):

    result = []

    
    for char, count in counter.items(): 
        if char.isalpha():
            result.append({"character": char, "count": count})

    result.sort(reverse=True, key=lambda x: x["count"])
    return result

print("============ BOOKBOT ============")
print(f"Analyzing book found at {full_path}...")
print("----------- Word Count ----------")
seperate_words()
print("--------- Character Count -------")
counter = character_counter()
sorted_result = sorter(counter)
for item in sorted_result:
        print(f"{item['character']}: {item['count']}")









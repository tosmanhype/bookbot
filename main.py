book_path = "books/frankenstein.txt"

def main():
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words()} words found in the document")
    
    letter_count = count_letter_sorted()
    
    for letter_result in letter_count:
        letter, counter = letter_result.items()
        print(f"The '{letter[1]}' character was found {counter[1]} times")
    
    print("--- End report ---")
    
def read_book() -> str:
    with open(book_path, "r") as f:
        file_contents = f.read()
    return file_contents

def count_words() -> int:
    book_content = read_book()
    return len(book_content.split())

def count_letters() -> dict:
    book_content = read_book()
    letter_counter = {}
    for letter in book_content:
        if str(letter).isalpha():
            letter_lower = str(letter).lower()
            if letter_lower in letter_counter:
                letter_counter[letter_lower] += 1
            else:
                letter_counter[letter_lower] = 1    
    return letter_counter

def count_letter_sorted() -> list[dict]:
    counter_dict = count_letters()
    result_list = []
    for letter in counter_dict:
        letter_result = {"name": letter, "count": counter_dict[letter]}
        result_list.append(letter_result)
    result_list.sort(reverse=True, key=sort_on_count)
    return result_list

def sort_on_count(result_dict):
    return result_dict["count"]

main()

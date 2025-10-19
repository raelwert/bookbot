import sys
from stats import count_words, count_characters, dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(sys.argv) == 1):
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    path_to_file = sys.argv[1]
    file_contents = get_book_text("./" + path_to_file)
    num_words = count_words(file_contents)
    num_chars = count_characters(file_contents)
    sorted_char_list = dict_to_sorted_list(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
         if item['char'].isalpha():
               print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
        main()
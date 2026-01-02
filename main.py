import sys
from stats import get_num_words, get_char_count, get_char_count_to_list_sorted

# BOOK_PATH = "books/frankenstein.txt" // hard coded

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
text = get_book_text(path)
char_count = get_char_count(text)

# frankenstein_text = get_book_text(BOOK_PATH) // hard coded

# char_count = get_char_count(frankenstein_text) // hard coded

# char_count_sorted = get_char_count_to_list_sorted // hard coded 

def main():
    # num_words = get_num_words(frankenstein_text)
    # print(f"Found {num_words} total words")
    # print(char_count) # print the dictionary of character counts
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in get_char_count_to_list_sorted(char_count):
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()
    """
    That line ensures the code inside the following block runs only when the file is executed as a script, not when it's imported as a module.

    Details:
    When Python runs a file directly, it sets the built-in variable name to "__main__".
    When the file is imported, name is the module's name (e.g., "my_module"), not "__main__".
    So:
    if name == "__main__": main()
    runs main() only when you do python your_file.py, preventing side effects (like printing or running code) when the file is imported elsewhere.
    """

# main() // main() is just being called above, this one is NOT needed

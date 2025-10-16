import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Use the argument as the book path
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        # Only print characters that are letters
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")

main()
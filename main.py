import sys
from stats import count_words, count_characters, get_sorted_list_of_dicts

def get_book_text(filepath):
    """Reads the text of a book from a given file path
    and returns it as a string.
    Args:
        filepath (str): The path to the book file.
    Returns:
        str: The text content of the book.
    """
    book_text = ""
    with open(f"{filepath}", 'r', encoding='utf-8') as file:
        book_text = file.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # book_path = "frankenstein.txt"
    
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_list = get_sorted_list_of_dicts(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    

main()

from stats import count_words, count_characters, sorted_list
import sys

args = sys.argv



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def report(book_path, count, sorted_list):
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}\n" \
    "----------- Word Count ----------\n" \
    f"Found {count} total words\n" \
    "--------- Character Count -------")
    for i in sorted_list:
        print(f"{i['char']}: {i['value']}")
    print("============= END ===============")
    



def main():
    try:
        book_path = args[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    count = count_words(text)
    letter_count = count_characters(text)
    list = sorted_list(letter_count)
    report(book_path, count, list)

if __name__ == "__main__":
    main()
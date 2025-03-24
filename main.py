from stats import count_words, count_chars, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_sys_argvs():
    if len(sys.argv) !=2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    return sys.argv[1]

def print_report(book_path, num_words, char_sorted_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    

    for char in char_sorted_list:
        if char['char'].isalpha():
            print(f'{char["char"]}: {char["count"]}')

    print('============= END ===============')
    
def main():
    book_path = get_sys_argvs()  
    text = get_book_text(book_path)

    count_of_words  = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_dict(char_count)
    print_report(book_path,count_of_words, sorted_char_count)


main()
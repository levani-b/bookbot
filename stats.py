    
def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    new_txt = text.lower()
    new_txt_lst = list(new_txt)
    for char in new_txt_lst:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count

def sort_on(dict):
    return dict['count']

def sort_dict(char_count):
    char_list = []
    for key, val in char_count.items():
        char_list.append({'char': key, 'count': val})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

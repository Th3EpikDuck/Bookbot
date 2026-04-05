def get_num_words(text):
    return len(text.split())
    
def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def sort_chars(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

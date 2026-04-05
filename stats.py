def get_num_words(text):
    new_text = text.split()
    return len(new_text)

def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_chars(text):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=get_num, reverse=True)
    return sorted_list

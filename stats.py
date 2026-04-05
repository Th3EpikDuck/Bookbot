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

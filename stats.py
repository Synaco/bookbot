def get_word_count(text):
    word_count = 0
    for words in text:
        word_count += 1
    return word_count


def get_char_dict(text):
    char_dict = {}
    for words in text:
        for char in words:
            if char.isalpha():
               if char.lower() in char_dict:
                   char_dict[char.lower()] += 1
               else:
                   char_dict[char.lower()] = 1
    return char_dict



def get_char_count(char_dict):
    pass

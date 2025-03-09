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
    char_dict_list = []
    for key, value in char_dict.items():
        char_dict_list.append({"key":key, "value":value})
    def sort_on(dict):
        return dict["value"]
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

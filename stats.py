def get_word_count(text):
    word_count = 0
    for words in text:
        word_count += 1
    return word_count


def get_char_dict(text):
    char_dict = {}
    char_list = []
    for char in text.split():
        if char.isalpha():
            char_list.append(char.lower())
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_char_count(char_dict):
    char_dict_list = []
    for key, value in char_dict.items():
        char_dict_list.append({"key":key, "value":value})
    def sort_on(dict):
        return dict["value"]
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

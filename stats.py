def count_words(string_of_text):
    word_count = 0
    word_list = string_of_text.split()
    word_count = len(word_list)
    return word_count

def count_characters(string_of_text):
    count_dict = {}
    text = string_of_text.lower()

    #check if letter is in count_dict
    for i in text: 
        if count_dict.get(i):
            char_var = count_dict[i] +1
            count_dict[i] = char_var
        else:
            count_dict[i] = 1
    return count_dict

def sorted_list(dict):
    sorted_list = []
    def sortfunc(e):
        return e["value"]
    for i in dict:
        if i.isalpha():
            tempdict = {"char": i, "value": dict[i]}
            sorted_list.append(tempdict)
    
    sorted_list.sort(key=sortfunc, reverse=True)
    return sorted_list
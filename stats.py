def word_count(file_contents):
    num_words=file_contents.split()
    word_total=len(num_words)
    return word_total

def character_count(file_contents):
    lowered=file_contents.lower()
    characters={}
    for character in lowered:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(d):
    return d["num"]

def sorted_character_list(num_chars_dict):
    sorted_list=[]
    for character in num_chars_dict:
        sorted_list.append({"char":character,"num":num_chars_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    

        
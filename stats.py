def count_words(text):
    """Counts the number of words in a given text.
    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    chardict = {}
    text = text.lower()
    for character in text:
        if character in chardict:
            chardict[character] += 1
        else: 
            chardict[character] = 1
    return chardict

def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key, "num": char_dict[key]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
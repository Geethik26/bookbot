def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Helper function that tells the sort method what to sort by
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    # Convert the dictionary into a list of dictionaries
    for char, num in num_chars_dict.items():
        sorted_list.append({"char": char, "num": num})
    
    # Sort the list from highest to lowest count
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
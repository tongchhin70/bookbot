def get_num_words(text):
    words = text.split()
    return len(words)

def count_unique_letters(text):
    count = {}
    
    words = text.lower().split()
    for word in words:
        for letter in word:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count

def sort_dict(word_dict):
    sorted_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict
import string

def repeated_word(str):
    str = str.translate(str.maketrans('', '', string.punctuation))
    all = {}
    words = str.split()
    for word in words:
        if  word.lower() in all:
            return word
        else:
            all[word.lower()] = 1
    return None
    a = {
        
    }
# def repeated_word(str):
#     str = str.translate(str.maketrans('', '', string.punctuation))
#     unique = []
#     all_words = str.split()
#     for word in all_words:
#         if word.lower() in unique:
#             return word.lower()
#         unique.append(word.lower())
#     return None


if __name__ == '__main__' :
    # print('K')
    print(repeated_word("Once upon a time, there was a brave princess who..."))

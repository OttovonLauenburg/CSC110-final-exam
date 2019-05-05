def print_max(word_list):
    word_occurence = {}
    for word in word_list:
        if word not in word_occurence:
            word_occurence[word] = 0
        word_occurence[word] += 1

    occurence_list = []
    for w in word_occurence:
        occurence_list.append(word_occurence[w])
    max_key = 0
    for key in occurence_list:
        if key > max_key:
            max_key = key

    for max_word in word_occurence:
        if word_occurence[max_word] == max_key:
            print(max_word)


input_word_list = ['the','tree','that','tree','the','tree']
print_max(input_word_list)
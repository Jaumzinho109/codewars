def get_count(sentence):
    lista = list(sentence.lower())
    count = 0
    for letter in lista:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1
        else:
            continue
    return count
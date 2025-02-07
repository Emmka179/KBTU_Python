def words_reverse():
    word = input("Enter a sentence: ").split()
    return word[::-1]

print(' '.join(words_reverse()))
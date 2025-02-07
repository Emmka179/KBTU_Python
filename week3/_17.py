def is_palindrome(str):
    str = ''.join(filter(str.isalnum, str))
    return str == str[::-1]

phrase = input("Enter a word: ")
print("Palindrome" if is_palindrome(phrase) else "Not palindrome")
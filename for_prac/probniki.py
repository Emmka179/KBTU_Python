def process_numbers():
    nums = [1, 2, 3, 5, 6]
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print(process_numbers())

#Используя мап и фильтер одновременно вывести квадраты чисел, если они четные


def all_words_capitalized():
    sentence = "Hello World This is Python" 
    return all(word[0].isupper() for word in sentence.split() if word.isalpha())
print(all_words_capitalized())

#Написать функцию, которая через all() проверяет начинаются ли все буквы данного предложения через заглавную. Вывести True/False

import re

f = input()
if re.fullmatch(f[::-1], f):
    print(f'{f} is palindrom')
else:
    print(f'{f} is not palindrom')

####

import re

f = input()
reversed_f = ''.join(reversed(f))

if re.fullmatch(re.escape(reversed_f), f):
    print(f'{f} is palindrom')
else:
    print(f'{f} is not palindrom')


#Написать функцию по определению палиндрома с помощью regex без использования срезов

import re

f = input()
if re.fullmatch(f[::-1], f):
    print(f'{f} is palindrom')
else:
    print(f'{f} is not palindrom')

#Та же функция но со срезами

import time
import math

num = int(input())
delay = int(input())

time.sleep(delay / 1000)  # Задержка в секундах

print(f"Square root of {num} after {delay} miliseconds is {math.sqrt(num)}")

# программа, которая вычисляет квадратный корень числа после задержки в заданное количество миллисекунд


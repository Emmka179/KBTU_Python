from itertools import permutations

def permutation():
    s = input("Enter smth: ")
    for _ in permutations(s):
        print("".join(_))
permutation()
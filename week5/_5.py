import re

f = open("C:/Users/bboya/OneDrive/Desktop/pp2/week5/row.txt", "r", encoding="utf-8")

pat = r'^a.*b$'
text = f.read().split()

for word in text:
    if re.fullmatch(pat, word):
        print(word)
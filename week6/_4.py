import os

try:
    with open("C:\\Users\\bboya\\OneDrive\\Desktop\\pp2\\week6\\laba.txt", "r") as file:
        print("Количество строк:", len(file.readlines()))
except:
    print("Ошибка:")
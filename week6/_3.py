import os

path = input("Введите путь для проверки: ")
if os.path.exists(path):
    print("Путь существует")
    print("Директория:", os.path.dirname(path))
    print("Файл:", os.path.basename(path))
else:
    print("Путь не существует")
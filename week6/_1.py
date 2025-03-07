import os

def list_contents(path):
    try:
        items = os.listdir(path)
        dirs = []
        files = []
        
        for item in items:
            if os.path.isdir(os.path.join(path, item)):
                dirs.append(item)
            else:
                files.append(item)
        
        print("Папки:", dirs)
        print("Файлы:", files)
        print("Все элементы:", items)
        
    except Exception as e:
        print("Ошибка:", e)

path = input("Введите путь: ")
list_contents(path)

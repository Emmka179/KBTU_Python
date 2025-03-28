import re

# 1. Поиск шаблона в строке
pattern = r'\d+'  # Ищем числа
text = 'Цена: 250 руб.'
match = re.search(pattern, text)
print(match.group() if match else 'Нет совпадений')

# 2. Поиск всех вхождений
matches = re.findall(pattern, text)
print(matches)  # ['250']

# 3. Разбиение строки по шаблону
pattern = r'\s+'  # Разделение по пробелам
text = 'Это тестовая строка'
words = re.split(pattern, text)
print(words)

# 4. Замена по шаблону
pattern = r'\d+'
text = 'Цена: 250 руб.'
new_text = re.sub(pattern, 'XXX', text)
print(new_text)  # Цена: XXX руб.

# 5. Проверка соответствия шаблону
pattern = r'^\d{3}$'  # Ровно три цифры
text = '123'
match = re.fullmatch(pattern, text)
print(bool(match))  # True

# 6. Группы захвата
pattern = r'(\d+)-(\d+)-(\d+)'
text = 'Дата: 2024-03-15'
match = re.search(pattern, text)
if match:
    print(match.group(1), match.group(2), match.group(3))  # 2024 03 15

# 7. Special Sequences
text = 'Python 3.10 is great!'
print(re.findall(r'\d+', text))  # ['3', '10']  # \d - цифры
print(re.findall(r'\D+', text))  # ['Python ', ' is great!']  # \D - не цифры
print(re.findall(r'\s+', text))  # [' ']  # \s - пробелы
print(re.findall(r'\S+', text))  # ['Python', '3.10', 'is', 'great!']  # \S - не пробелы
print(re.findall(r'\w+', text))  # ['Python', '3', '10', 'is', 'great']  # \w - буквы, цифры, _
print(re.findall(r'\W+', text))  # [' ', '.', ' ', '!']  # \W - не буквы, не цифры, не _

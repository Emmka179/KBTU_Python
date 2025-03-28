# Преобразование Python-объекта в JSON
data = {'name': 'Alex', 'age': 25, 'city': 'Moscow'}
json_data = json.dumps(data, indent=4)
print(json_data)  # {
#    "name": "Alex",
#    "age": 25,
#    "city": "Moscow"
# }

# Чтение JSON-строки и преобразование в Python-объект
json_string = '{"name": "Alex", "age": 25, "city": "Moscow"}'
data = json.loads(json_string)
print(data['name'])  # Alex

# Запись JSON в файл
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Чтение JSON из файла
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
print(loaded_data)  # {'name': 'Alex', 'age': 25, 'city': 'Moscow'}
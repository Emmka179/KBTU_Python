def multiply_list():
    numbers = input("Введите числа через пробел: ").split()
    numbers = [int(num) for num in numbers]
    result = 1
    for num in numbers:
        result *= num
    print("Результат умножения:", result)
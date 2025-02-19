def square_gen(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
for _ in square_gen(a, b):
    print(_)
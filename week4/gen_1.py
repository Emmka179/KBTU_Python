def square_gen(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input("Enter a number: "))
for _ in square_gen(n):
    print(_)
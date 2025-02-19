def it_num(n):
    for i in range(n, -1, -1):
        yield i
        
n = int(input('Enter a number: '))

print(", ".join(map(str, it_num(n))))
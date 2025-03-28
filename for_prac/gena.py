a = int(input())
def func(a):
    for num in range(0, a+1):
        yield a-num
print(list(func(a)))
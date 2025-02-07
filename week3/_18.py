def histogram(l):
    for num in l:
        print('*' * num)

l = list(map(int, input("Enter numbers separated by spaces: ").split()))
histogram(l)
file = input().split()
with open("C:\\Users\\bboya\\OneDrive\\Desktop\\pp2\\week6\\laba.txt", 'w') as f:
    for _ in file:
        f.write(_+'\n')
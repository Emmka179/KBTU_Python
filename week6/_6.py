for i in range(ord('A'), ord('Z') +1):
    path = f"C:\\Users\\bboya\\OneDrive\\Desktop\\pp2\\week6\\files/{chr(i)}.txt"
    with open(path, 'w') as file:
        file.write(chr(i))
def count_case(s):
    upper, lower = 0, 0
    for c in s:
        if c.isupper(): upper += 1
        elif c.islower(): lower += 1
    print("Большие буквы:", upper, "Маленькие буквы:", lower)
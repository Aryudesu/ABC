def calc(Y):
    if Y % 400 == 0:
        return 366
    if Y % 100 == 0:
        return 365
    if Y % 4 == 0:
        return 366
    return 365

print(calc(int(input())))

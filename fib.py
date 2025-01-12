a, b, c, d = 1, 0, 0, 0
while a < 3000 and b < 3000 and c < 3000 and d < 3000:
    a, b, c, d = a + b + c, a, b, c
    print(a, b, c, d)

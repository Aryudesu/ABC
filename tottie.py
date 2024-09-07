for a in range(1, 1000000):
    for b in range(1, 1000000):
        if (a + b) ** 2 == int(f"{a}{b}"):
            print(a, b)

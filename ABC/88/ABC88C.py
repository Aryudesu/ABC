def calc(c):
    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                f = True
                for i in range(3):
                    if c[0][i] - a1 != c[1][i] - a2 or c[1][i] - a2 != c[2][i] - a3:
                        f = False
                if f:
                    return True
    return False


c = []
for i in range(3):
    c.append([int(l) for l in input().split()])
print("Yes" if calc(c) else "No")

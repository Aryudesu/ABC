def calc(N: int, X: int, Y: int):
    data = set()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            data.add((i + j, i * j))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if Y % (i * j) > 0:
                continue
            tmp = (X - (i + j), Y // (i * j))
            if tmp in data:
                return True
    return False



N, X, Y = [int(l) for l in input().split()]
print("Yes" if calc(N, X, Y) else "No")

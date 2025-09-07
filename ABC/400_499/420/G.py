def calcNM(a, b):
    m4 = a + b
    n4_2 = a - b
    if m4 < 0:
        return None
    return [(a - b - 2)//4, (b - a - 2)//4]

X = int(input())
result = []
memo = set()
for k in range(X):
    Y = 4*X - 1
    if k * k > Y:
        break
    if Y % k != 0:
        continue
    a, b = k, Y // k
    m4 = a + b
    n4_2 = a - b

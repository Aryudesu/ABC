def calc2(Data, y, x):
    dy = y // N
    dx = x // N
    ey = y % N
    ex = x % N
    result = dy * dx * Data[-1][-1]
    result += dx * Data[ey][-1]
    result += dy * Data[-1][ex]
    result += Data[ey][ex]
    return result


def calc(Data, A, B, C, D):
    dy = A // N
    dx = B // N
    a = A % N
    b = B % N
    c = C - N * dy
    d = D - N * dx
    result = calc2(Data, c, d)
    if a > 0 and d > 0:
        result -= calc2(Data, a - 1, d)
    if b > 0 and c > 0:
        result -= calc2(Data, c, b - 1)
    if a > 0 and b > 0:
        result += calc2(Data, a-1, b-1)
    return result


N, Q = [int(l) for l in input().split()]
P = []
for n in range(N):
    tmp = input()
    P.append(tmp)

Data = []
s = 0
dat = []
for i in range(N):
    if P[0][i] == "B":
        s += 1
    dat.append(s)
Data.append(dat)
for i in range(1, N):
    dat = []
    s = 0
    for j in range(N):
        if P[i][j] == "B":
            s += 1
        dat.append(Data[i-1][j] + s)
    Data.append(dat)
result = []
for q in range(Q):
    a, b, c, d = [int(l) for l in input().split()]
    result.append(calc(Data, a, b, c, d))
for r in result:
    print(r)

def calcP(x: int, Y: int, K: int)->int:
    l, r = x, x
    if l <= Y <= r:
        return 0
    c = 0
    while l < Y:
        c += 1
        l = l * K
        r = r * K + K - 1
        if l <= Y <= r:
            return c
    return None

def calc(X: int, Y: int, K: int)->int:
    x = X
    if X == Y:
        return 0
    tmp = calcP(x, Y, K)
    if tmp is not None:
        return tmp
    c = 0
    while x > 0:
        c += 1
        x //= K
        tmp = calcP(x, Y, K)
        if tmp is not None:
            return c + tmp
    raise ValueError()


T = int(input())
result = []
for _ in range(T):
    x, y, k = map(int, input().split())
    result.append(calc(x, y, k))
for r in result:
    print(r)

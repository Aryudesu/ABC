def calc(X, Y):
    MOD = 10 ** 9 + 7
    if (2 * X - Y) % 3 or (2 * X - Y) < 0 or (2 * Y - X) % 3 or (2 * Y - X) < 0:
        return 0
    a = (2 * Y - X) // 3
    b = (2 * X - Y) // 3
    res1 = 1
    for i in range(a + b, b, -1):
        res1 = (res1 * i) % MOD
    res2 = 1
    for i in range(1, a + 1):
        res2 = (res2 * i) % MOD
    return (res1 * pow(res2, MOD-2, MOD)) % MOD


X, Y = [int(l) for l in input().split()]
print(calc(X, Y))

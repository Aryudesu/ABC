def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)

MOD = 998244353

def calc(N):
    if N == 1:
        return 0, 0
    ay = 1
    ax = N + 1
    by = N
    bx = N + 1
    resA = ay * inverseMod(ax, MOD)
    resB = by * inverseMod(bx, MOD)
    return resA, resB

# N = int(input())
# result = calc(N)
# print(*result)
N = 1000
for n in range(1, N):
    for m in range(1, N):
        tmp = (n * inverseMod(m, MOD)) % MOD
        if tmp == 174692763:
            print(n, m, tmp)

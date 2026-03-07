from collections import defaultdict
MOD = 1000000007
def calc(N: int, P: int, A: list[int]):
    data = defaultdict(int)
    A.sort()
    if P != 0:
        result = 0
        for a in A:
            if a == 0:
                continue
            b = (pow(a%MOD, MOD - 2, MOD) * P) % MOD
            result += data[b]
            data[a % MOD] += 1
        return result
    else:
        zeroCount = A.count(0)
        return zeroCount * (N - zeroCount) + zeroCount * (zeroCount - 1)//2

N, P = [int(l) for l in input().split()]
A = [int(l)%MOD for l in input().split()]
print(calc(N, P, A))

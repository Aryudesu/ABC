from collections import defaultdict

def calc(N, P, A):
    data = defaultdict(int)
    for a in A:
        data[a % MOD] += 1

    if P != 0:
        result = 0
        for a in A:
            b = (pow(a, MOD - 2, MOD) * P) % MOD
            if a % MOD == b:
                result += data[b] - 1
            else:
                result += data[b]
        return result // 2
    



MOD = 1000000007
N, P = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(calc(N, P, A))

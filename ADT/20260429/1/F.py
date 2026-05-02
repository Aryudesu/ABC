from collections import defaultdict

def calc(N: int, L: int, D: list[int])->int:
    if L % 3:
        return 0
    p = 0
    data = defaultdict(int)
    data[0] += 1
    for i in range(N-1):
        p += D[i]
        p %= L
        data[p] += 1
    l = L // 3
    result = 0
    for p in data:
        q = (p + l) % L
        if q in data:
            r = (q + l) % L
            if r in data:
                result += data[p] * data[q] * data[r]
    return result//3

N, L = map(int, input().split())
D = list(map(int, input().split()))
print(calc(N, L, D))

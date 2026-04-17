from itertools import product

MOD = 10**9 + 7

def getData(data: list[int], M: int)-> int:
    result = [dict() for _ in range(len(data) + 1)]
    for dat in product([0, 1], repeat=len(data)):
        s = 0
        c = 0
        for f, n in zip(dat, data):
            if f:
                s = (s + n) % M
                c += 1
        result[c][s] = (result[c].get(s, 0) + 1) % MOD
    return result
        

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
T = N // 2
B = A[T:]
A = A[:T]
result = 0
resA: list[dict[int, int]] = getData(A, M)
resB: list[dict[int, int]] = getData(B, M)
# print(resA)
# print(resB)
# Aからnum人選んだ
for num in range(len(resA)):
    if K - num < 0:
        continue
    if num > K:
        continue
    if K - num >= len(resB):
        continue
    # print("debug", num, K-num)
    # BからはK-num人選ぶ必要がある
    bData = resB[K - num]
    for aSum, count in resA[num].items():
        bSum = (M - aSum) % M
        bCount = bData.get(bSum, 0)
        result = (result + count * bCount) % MOD
print(result)


from itertools import permutations
from typing import Tuple

def calcReplacementNum(arr: Tuple[int], N: int)-> int:
    """配列が何回置換が行われた結果できるのか計算します"""
    # サイクル分解の手法が早いらしい  はやいのか？？？　　飯食べてきます　(・ω・)ﾉｼ
    memo = [False] * N
    result = 0
    for i in range(N):
        if memo[i]:
            continue

    return result

# === AWC0010E

N, K = map(int, input().split())
C = []
for n in range(N):
    C.append(list(map(int, input().split())))

result = 0
for dat in permutations(range(N)):
    if calcReplacementNum(dat, N) > K:
        continue
    tmp = 0
    for i in range(N):
        a, b = dat[i], dat[i-1]
        tmp += C[a][b]
    result = max(result, tmp)
print(result)


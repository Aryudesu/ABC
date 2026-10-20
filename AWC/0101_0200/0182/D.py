# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
from typing import Tuple

INF = 10 ** 18
def calc(N: int, M: int, A: list[int], LRCW: list[Tuple[int, int, int, int]], mask: int)->int:
    imos = [0] * (N + 1)
    result = 0
    for m in range(M):
        b = 1 << m
        if not (mask & b):
            continue
        l, r, c, w = LRCW[m]
        result += w
        imos[l-1] += c
        imos[r] -= c
    s = 0
    for n in range(N):
        s += imos[n]
        if A[n] > s:
            return INF
    return result


N, M = map(int, input().split())
A = list(map(int, input().split()))
LRCW = []
for _ in range(M):
    l, r, c, w = map(int, input().split())
    LRCW.append((l, r, c, w))
result = INF
for mask in range(1 << M):
    res = calc(N, M, A, LRCW, mask)
    result = min(result, res)
print(result if result < INF else -1)

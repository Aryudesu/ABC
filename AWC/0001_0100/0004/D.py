from heapq import heappop, heappush
from typing import Tuple

def calc(N: int, M: int, LR: list[Tuple[int, int]])->bool:
    LR.sort()
    if N < M:
        return False
    if M == 0:
        return True
    data = []
    idx = 0
    for i in range(1, N + 1):
        while idx < M and LR[idx][0] <= i:
            l, r = LR[idx]
            heappush(data, r)
            idx += 1
        if len(data) == 0:
            continue
        r = heappop(data)
        if r < i:
            return False
    return (idx == M and len(data) == 0)


N, M = map(int, input().split())
LR = []
for m in range(M):
    l, r = map(int, input().split())
    LR.append((l, r))
print("Yes" if calc(N, M, LR) else "No")

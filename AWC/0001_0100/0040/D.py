from typing import Tuple
from heapq import heappop, heappush

def reachable(N, G, F, PR: list[Tuple[int, int]])->bool:
    """ゴールに辿り着くことはできるか"""
    now = F
    for p, r in PR:
        if now - p < 0:
            return False
        now += r
    if now - G < 0:
        return False
    return True

def calc(N, G, F, PR: list[Tuple[int, int]])->int:
    """計算の予定"""
    oil = F
    data = []
    result = 0
    for p, r in PR:
        while oil - p < 0:
            tmp = -heappop(data)
            oil += tmp
            result += 1
        heappush(data, -r)
    while oil - G < 0:
        tmp = -heappop(data)
        oil += tmp
        result += 1
    return result

N, G, F = map(int, input().split())
PR = []
for n in range(N):
    p, r = map(int, input().split())
    PR.append((p, r))
PR.sort()
if not reachable(N, G, F, PR):
    print(-1)
    exit(0)
print(calc(N, G, F, PR))

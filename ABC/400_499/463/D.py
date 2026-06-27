from typing import Iterable, Tuple

def maxNonOverlappingIntervals(intervals: Iterable[Tuple[int, int]], gap: int=0, sort: bool = True)-> list[Tuple[int, int]]:
    """[l, r)の区間列挙"""
    LR = intervals
    if sort:
        LR: list[Tuple[int, int]] = sorted(LR, key = lambda x: (x[1], x[0]))
    cur = -10 ** 30
    result = []
    for l, r in LR:
        if cur <= l:
            result.append((l, r))
            cur = r + gap
    return result

def isOk(K: int, gap: int, LR: list[Tuple[int, int]])->bool:
    res = maxNonOverlappingIntervals(LR, gap, False)
    return len(res) >= K

def calc(K: int, LR: list[Tuple[int, int]])->int:
    l = -1
    r = 1000000001
    while r - l > 1:
        mid = (r + l) // 2
        if isOk(K, mid, LR):
            l = mid
        else:
            r = mid
    return l

N, K = map(int, input().split())
LR = []
for n in range(N):
    l, r = map(int, input().split())
    LR.append((l, r))
LR = sorted(LR, key = lambda x: (x[1], x[0]))
if isOk(K, 1, LR):
    print(calc(K, LR))
else:
    print(-1)

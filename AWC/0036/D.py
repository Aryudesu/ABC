from typing import Iterable, Tuple

def calc(intervals: Iterable[Tuple[int, int]])-> int:
    """[l, r)の区間列挙"""
    LR: list[Tuple[int, int]] = sorted(intervals, key = lambda x: x[1])
    INF = 10 ** 30
    cur = [-INF]
    result = 0
    for l, r in LR:
        if l >= cur:
            result += 1
            cur = r
    return result


N = int(input())
SE = []
for n in range(N):
    s, e = map(int, input().split())
    SE.append((s, e))

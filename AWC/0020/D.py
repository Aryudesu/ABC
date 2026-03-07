from typing import Tuple

def mergeIntervals(data: list[Tuple[int, int]])-> list[Tuple[int, int]]:
    """半開区間[L, R)の範囲結合を行います．"""
    if len(data) == 0:
        return []
    data.sort()
    result = [data[0]]
    for l, r in data[1:]:
        pl, pr = result[-1]
        if l <= pr:
            result[-1] = (pl, max(pr, r))
        else:
            result.append((l, r))
    return result


N, L = map(int, input().split())
intervals = []
for n in range(N):
    x, r = map(int, input().split())
    intervals.append((x-r, x+r))
interval = mergeIntervals(intervals)
if len(interval) != 1:
    print("No")
else:
    l, r = interval[0]
    # print(l, r)
    if l <= 0 and L <= r:
        print("Yes")
    else:
        print("No")

from collections import defaultdict
from bisect import bisect_left, bisect_right

def calcLastIdx(N: int, T: str, startIdx: int, cIdx: dict[str, list[int]])->int:
    # print(cIdx)
    nowIdx = startIdx-1
    for t in T:
        idxes = cIdx.get(t)
        if idxes is None:
            return N
        k = bisect_left(idxes, nowIdx)
        if len(idxes) <= k:
            return N
        nextIdx = idxes[k]
        if nowIdx == nextIdx:
            k += 1
            if len(idxes) <= k:
                return N
            nextIdx = idxes[k]
        # print(t, nowIdx, nextIdx)
        nowIdx = nextIdx
    return nowIdx

S = input()
T = input()
cIdx = defaultdict(list)
for i in range(len(S)):
    s = S[i]
    cIdx[s].append(i)
# print(cIdx)
result = 0
for i in range(len(S)):
    lastIdx = calcLastIdx(len(S), T, i, cIdx)
    result += lastIdx - i
    # print("lastIdx", lastIdx)
print(result)

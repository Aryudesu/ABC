from bisect import bisect_right
from collections import defaultdict
from atcoder.segtree import SegTree

N, M = map(int, input().split())
LR = []
RL = []
leftList = [-1] * (N + 3)
rightList = [N + 5] * (N + 3)
lrCounter = defaultdict(int)
for m in range(M):
    l, r = map(int, input().split())
    LR.append((l, r))
    RL.append((r, l))
    leftList[r] = max(leftList[r], l)
    rightList[l] = min(rightList[l], r)
    lrCounter[(l, r)] += 1
maxST = SegTree(max, -1, leftList)
minST = SegTree(min, N + 10, rightList)
LR.sort()
RL.sort()


def check(M, s, t, LR, RL, lIdx, rIdx, lrCounter)->bool:
    if lIdx < 0 or lIdx >= M:
        return False
    ll, lr = LR[lIdx]
    if rIdx < 0 or rIdx >= M:
        return False
    rr, rl = RL[rIdx]

    if ll == rl and lr == rr:
        if lrCounter[(ll, lr)] == 1:
            return False
    if ll <= rl <= lr <= rr and ll == s and rr == t:
        return True
    if ll <= lr < rl <= rr and lr + 1 == rl and ll == s and rr == t:
        return True
    return False

searchRange = 2
result = []
Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    isOk = False
    if (s, t) in lrCounter:
        if lrCounter[(s, t)] >= 2:
            isOk = True
        elif lrCounter[(s, t)] == 1:
            tmp = maxST.prod(s, t)
            if s <= tmp <= t:
                isOk = True
            if not isOk:
                tmp = minST.prod(s + 1, t + 1)
                if s <= tmp <= t:
                    isOk = True 

    if not isOk:
        lrIdx = bisect_right(LR, (s, t))
        rlIdx = bisect_right(RL, (t, s))
        for i in range(-searchRange, searchRange + 1):
            for j in range(-searchRange, searchRange + 1):
                if check(M, s, t, LR, RL, lrIdx + i, rlIdx - j, lrCounter):
                    isOk = True
                    break
            if isOk:
                break
    
    result.append("Yes" if isOk else "No")

for res in result:
    print(res)

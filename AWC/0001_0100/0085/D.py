from collections import defaultdict
from typing import Tuple

class PrefixSum:
    """1次元累積和ライブラリ"""
    def __init__(self, arr: list[int]):
        self.pref = [0]
        for x in arr:
            self.pref.append(self.pref[-1] + x)

    def sum(self, l: int, r: int) -> int:
        """[l, r)の累積和を計算します"""
        return self.pref[r] - self.pref[l]

    def allSum(self) -> int:
        """全ての和を計算します"""
        return self.pref[-1]
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            l = 0 if key.start is None else key.start
            r = len(self.pref)-1 if key.stop is None else key.stop
            return self.pref[r] - self.pref[l]
        return self.pref[key]

N, M, Q = map(int, input().split())
RESULT = [None] * Q
A = list(map(int, input().split()))
ps = PrefixSum(A)
PCDQ = defaultdict(list)
for q in range(Q):
    p, c, d = input().split()
    p, d = int(p), int(d)
    # 元となる状態→次になってほしい状態
    PCDQ[p].append((c, d, q+1))

# Aのうち[l, r)が残っていて，lidxからridxの間に位置する．l=rのとき何も残っていない．
def calc(N: int, M: int, node: int, PCDQ: dict[int, Tuple[int, int, int, int]], l: int, r: int, lidx: int, ridx: int, ps: PrefixSum)->int:
    # 次の操作
    prev = 0
    if 0 <= l < N and 0 <= r <= N:
        prev = ps[l:r]
    for c, d, q in PCDQ[node]:
        nextL = l
        nextR = r
        if c == "L":
            nextLidx = lidx - d
            nextRidx = ridx - d
            if nextRidx < 1:
                nextL = 0
                nextR = 0
            elif nextLidx < 1:
                nextL = min(N, l - nextLidx)
                nextR = r
                if nextL > nextR:
                    nextL = nextR
            nextLidx = max(1, nextLidx)
            nextRidx = max(1, nextRidx)
        else:
            nextLidx = lidx + d
            nextRidx = ridx + d
            if nextLidx > M:
                nextL = 0
                nextR = 0
            elif nextRidx > M:
                nextR = max(0, min(N, r - (nextRidx - M)))
                nextL = l
                if nextL > nextR:
                    nextL = nextR
            nextLidx = min(M, nextLidx)
            nextRidx = min(M, nextRidx)
        RESULT[q-1] = prev - ps[nextL: nextR]
        calc(N, M, q, PCDQ, nextL, nextR, nextLidx, nextRidx, ps)

calc(N, M, 0, PCDQ, 0, N, 1, N, ps)
for r in RESULT:
    print(r)

from bisect import bisect_left
from typing import List

class LISolver:
    """最長増加部分列の取得"""
    def __init__(self, A: List[int]) -> None:
        """初期化"""
        self.A = A
        self.N = len(A)
        self._length = 0
        self._subseq = []
        self._solved = False

    def _solve(self) -> None:
        """LIS復元"""
        A = self.A
        N = self.N
        INF = float('inf')

        dp_val = []       # 長さiの増加列の末尾最小値
        dp_index = []     # それに対応するAのインデックス
        pos = [0]*N       # A[i]が何番目の位置に入ったか
        prev = [-1]*N     # 復元のための前インデックス

        for i, a in enumerate(A):
            idx = bisect_left(dp_val, a)
            if idx == len(dp_val):
                dp_val.append(a)
                dp_index.append(i)
            else:
                dp_val[idx] = a
                dp_index[idx] = i
            pos[i] = idx
            if idx > 0:
                prev[i] = dp_index[idx - 1]

        # 復元
        length = len(dp_val)
        cur = -1
        for i in range(N - 1, -1, -1):
            if pos[i] == length - 1:
                cur = i
                break

        subseq = []
        while cur != -1:
            subseq.append(A[cur])
            cur = prev[cur]
        subseq.reverse()

        self._length = length
        self._subseq = subseq
        self._solved = True

    def length(self) -> int:
        """最長増加部分列の長さを返す"""
        if not self._solved:
            self._solve()
        return self._length

    def restore(self) -> List[int]:
        """最長増加部分列の具体的な列を返す"""
        if not self._solved:
            self._solve()
        return self._subseq[:]

N = int(input())
P1 = list(map(int, input().split()))
lis1 = LISolver(P1)
l1 = lis1.length()
ll1 = lis1.restore()
ll1s = set(ll1)
P2 = []
for p in P1:
    if p not in ll1s:
        P2.append(p)
lis2 = LISolver(P2)
l2 = lis2.length()
ll2 = lis2.restore()
ll2s = set(ll2)
l1idx = 0
P3 = []
for idx in range(N):
    if l1idx < l1 and ll1[l1idx] == P1[idx]:
        l1idx += 1
        continue
    if P1[idx] not in ll2s and P1[idx] not in ll1s:
        if l1idx + 1 < l1 and ll1[l1idx] < P1[idx] < ll1[l1idx + 1]:
            continue
        else:
            if not P3 or P3[-1] < P1[idx]:
                P3.append(P1[idx])
    if P3 and P3[-1] < P1[idx]:
            P3.append(P1[idx])
if P3:
    l2 = len(P3)
# print(P3)
print(l1 + l2)

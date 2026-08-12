from sortedcontainers import SortedDict
from collections import deque

class OriginRectangleUnion:
    """
    原点を左下とする長方形 [0, x] × [0, y] を追加し、
    和集合面積を管理する。

    add(x, y):
        長方形 [0, x] × [0, y] を追加。

    area:
        現在の和集合面積。

    内部では Pareto frontier を階段状に保持する。

    計算量:
        add 1回あたり償却 O(log N)
    """

    INF = 1 << 60

    def __init__(self):
        self._frontier = SortedDict({
            0: self.INF,
            self.INF: 0,
        })
        self.area = 0

    def add(self, x: int, y: int) -> None:
        mp = self._frontier

        pos = mp.bisect_left(x)
        rx = mp.keys()[pos]

        # 既存領域に包含される
        if mp[rx] >= y:
            return

        # 新しい点に支配される境界点を削除
        while True:
            pos = mp.bisect_left(x)
            lx = mp.keys()[pos - 1]
            ly = mp[lx]

            if ly > y:
                break

            li = mp.bisect_left(lx)
            plx = mp.keys()[li - 1]
            nrx = mp.keys()[li + 1]

            self.area -= (lx - plx) * (ly - mp[nrx])
            del mp[lx]

        # 新しい境界点を挿入
        pos = mp.bisect_left(x)
        lx = mp.keys()[pos - 1]
        rx = mp.keys()[pos]

        self.area += (x - lx) * (y - mp[rx])
        mp[x] = y


N = int(input())
A = list(map(int, input().split()))

# original value v を v+1 にずらして、
# 1-origin mex の問題として考える。
#
# mex に必要なのは 1..N だけなので、
# original A=N は無視してよい。
pos = [deque() for _ in range(N + 1)]

for i, a in enumerate(A, 1):
    b = a + 1
    if b <= N:
        pos[b].append(i)

# 「これ以降には出現しない」番兵
for v in range(1, N + 1):
    pos[v].append(N + 1)

ar = OriginRectangleUnion()

# 左端 l=1 のときの各値の next occurrence を登録
for v in range(1, N + 1):
    nxt = pos[v][0]
    ar.add(N + 1 - v, nxt)

ans = 0

for i, a in enumerate(A, 1):
    # 現在の左端 i に対する寄与
    #
    # sum_{k=1..N} (N+1 - max(next[1],...,next[k]))
    #
    # = N(N+1) - ar.area
    ans += N * (N + 1) - ar.area

    # 左端を i -> i+1 に進める。
    # A[i]+1 の next occurrence だけが更新される。
    v = a + 1

    if v <= N:
        pos[v].popleft()
        nxt = pos[v][0]
        ar.add(N + 1 - v, nxt)

print(ans)

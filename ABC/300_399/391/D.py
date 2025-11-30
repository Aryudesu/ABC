from collections import defaultdict
from sortedcontainers import SortedSet

class Gravity:
    def __init__(self, N: int, W: int):
        self.N = N
        self.W = W
        # times[n] = t 何もなく最後に1段目にブロックが着地するであろう時間
        self.times = dict()
        # xに存在する個数
        self.count = [0] * W
        self.blocks = defaultdict(list)
        self.exists = set(range(N))
    
    def add(self, XY: list[list[int]]):
        # 低いところにある順に処理
        YX = [[XY[n][1], XY[n][0], n] for n in range(self.N)]
        YX.sort()
        for y, x, n in YX:
            h = self.count[x]
            self.count[x] += 1
            self.blocks[h].append(n)
            if self.times.get(h) is None:
                self.times[h] = y
            else:
                self.times[h] = max(self.times[h], y)

    def calc(self, TA: list[list[int]])-> list[int]:
        result = [None] * len(TA)
        TAN = []
        for n in range(len(TA)):
            t, a = TA[n]
            TAN.append((t, a, n))
        TAN.sort()
        # 時間
        now = 0
        # 高さ
        h = 0
        # クエリ用
        idx = 0
        # 時刻tの時点で消えるものは最初から消しておく
        if len(self.blocks[h]) == self.W and self.times.get(h) == 0:
            for b in self.blocks[h]:
                self.exists.discard(b)
            h += 1
        # 消え続けるまで続ける
        while len(self.blocks[h]) == self.W:
            # 次のブロックが消える直前
            next_time = max(self.times[h] + 1, now + 1)
            while idx < len(TAN):
                t, a, n = TAN[idx]
                if t >= next_time:
                    break
                result[n] = a in self.exists
                idx += 1
            if idx >= len(TAN):
                break
            # 消えるブロック一覧
            for b in self.blocks[h]:
                self.exists.discard(b)
            now = next_time
            h += 1
        while idx < len(TAN):
            t, a, n = TAN[idx]
            result[n] = a in self.exists
            idx += 1
        return result


N, W = map(int, input().split())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x-1, y-1))
g = Gravity(N, W)
g.add(XY)
Q = int(input())
TA = []
for _ in range(Q):
    t, a = map(int, input().split())
    TA.append((t, a-1))
result = g.calc(TA)
for r in result:
    print("Yes" if r else "No")

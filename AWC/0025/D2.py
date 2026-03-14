class FunctionalGraph:
    """Functional Graph の始点からの遷移解析"""

    def __init__(self, to: list[int], start: int):
        self.to = to
        self.start = start
        self.order = []
        self.pos = {}
        self.loop_start = -1
        self.loop = []
        self._build()

    def _build(self) -> None:
        now = self.start
        while now not in self.pos:
            self.pos[now] = len(self.order)
            self.order.append(now)
            now = self.to[now]

        self.loop_start = self.pos[now]
        self.loop = self.order[self.loop_start:]

    def kth(self, k: int) -> int:
        """start から k 回遷移した先を返す"""
        if k < len(self.order):
            return self.order[k]
        return self.loop[(k - self.loop_start) % len(self.loop)]

    def is_in_loop(self, v: int) -> bool:
        """v が start から到達するループ部分に含まれるか"""
        return v in self.pos and self.pos[v] >= self.loop_start

N, S, Q = map(int, input().split())
X = list(map(int, input().split()))
data = [(X[n], n) for n in range(N)]
data.sort()
graph = [None] * N
for idx in range(N):
    x, n = data[idx]
    if idx == 0:
        graph[data[idx][1]] = data[1][1]
        continue
    elif idx == N-1:
        graph[data[idx][1]] = data[idx-1][1]
        continue
    l = data[idx][0] - data[idx-1][0]
    r = data[idx+1][0] - data[idx][0]
    if l > r:
        graph[data[idx][1]] = data[idx+1][1]
    elif l < r:
        graph[data[idx][1]] = data[idx-1][1]
    else:
        graph[data[idx][1]] = min(data[idx-1][1], data[idx+1][1])

fg = FunctionalGraph(graph, S-1)
print(fg.kth(Q) + 1)

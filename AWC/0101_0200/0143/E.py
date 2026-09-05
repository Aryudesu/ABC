from collections import defaultdict
from sortedcontainers import SortedSet

class EulerTourTree:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.euler = []
        self.first = dict()
        self.depth = []
        self.seg_tree = []
        self.subtree_size = dict()
        self.time_in = dict()
        self.time_out = dict()
        self.timer = 0

    def add_edge(self, u, v):
        """グラフに辺を追加（defaultdictを活用）"""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, p, d):
        """DFSでオイラーツアーを構築"""
        self.first[v] = len(self.euler)
        self.time_in[v] = self.timer
        self.timer += 1
        self.euler.append(v)
        self.depth.append(d)
        self.subtree_size[v] = 1

        for to in self.graph[v]:
            if to == p:
                continue
            self.dfs(to, v, d + 1)
            self.euler.append(v)
            self.depth.append(d)
            self.subtree_size[v] += self.subtree_size[to]

        self.time_out[v] = self.timer
        self.timer += 1

    def build(self, root=0):
        """木を構築してオイラーツアーとRMQを用意"""
        self.dfs(root, -1, 0)
        self._build_rmq()

    def _build_rmq(self):
        """RMQ (Sparse Table) を構築"""
        m = len(self.euler)
        log_m = (m - 1).bit_length()
        self.seg_tree = [[0] * m for _ in range(log_m)]
        self.seg_tree[0] = list(range(m))

        for i in range(1, log_m):
            for j in range(m - (1 << i) + 1):
                left = self.seg_tree[i - 1][j]
                right = self.seg_tree[i - 1][j + (1 << (i - 1))]
                self.seg_tree[i][j] = (
                    left if self.depth[left] < self.depth[right] else right
                )

    def get_lca(self, u, v):
        """LCA (最小共通祖先) を求める"""
        l, r = self.first[u], self.first[v]
        if l > r:
            l, r = r, l
        log_len = (r - l + 1).bit_length() - 1
        left = self.seg_tree[log_len][l]
        right = self.seg_tree[log_len][r - (1 << log_len) + 1]
        return (
            self.euler[left]
            if self.depth[left] < self.depth[right]
            else self.euler[right]
        )

    def get_subtree_size(self, v):
        """部分木のサイズを取得"""
        return self.subtree_size.get(v, 0)

    def is_ancestor(self, u, v):
        """u が v の祖先か判定"""
        return (
            self.time_in[u] <= self.time_in[v] and self.time_out[v] <= self.time_out[u]
        )

    def get_path_length(self, u, v):
        """u から v へのパスの長さ"""
        lca = self.get_lca(u, v)
        return (self.depth[self.first[u]] - self.depth[self.first[lca]]) + (
            self.depth[self.first[v]] - self.depth[self.first[lca]]
        )


N, Q = map(int, input().split())
P = list(map(int, input().split()))
graph = [-1]
for p in P:
    graph.append(p-1)

ett = EulerTourTree(N)
for u in range(N):
    ett.add_edge(u, graph[u])
ett.build(root=0)

for _ in range(Q):
    K, *Tmp = map(int, input().split())
    V = []
    U = SortedSet()
    for v in Tmp:
        V.append(v - 1)
        U.add((v - 1, 1))
    dist = 0
    minDist = N * N
    if K > 1:
        first = N
        firstNum = 0
        second = N
        secondNum = 0
        while len(U) > 1:
            p, num = U.pop()
            if first > p:
                second = first
                secondNum = firstNum
                first = p
                firstNum = num
            elif second > p:
                second = p
                secondNum = num
            if p > 0:
                U.add((graph[p], num))
        p, num = U.pop()
        if first > p:
            second = first
            secondNum = firstNum
            first = p
            firstNum = num
        elif second > p:
            second = p
            secondNum = num
        # print("debug", first, second)
        for v in V:
            dist += ett.get_path_length(first, v)
        for v in V:
            lca = ett.get_lca(second, v)
            if secondNum == K-1:
                if lca == second:
                    minDist = min(minDist, dist - ett.get_path_length(first, v))
                else:
                    fs = ett.get_path_length(first, second)
                    d = ett.get_path_length(first, v)
                    minDist = min(minDist, dist - d - fs * (N-1))
            else:
                minDist = min(minDist, dist - ett.get_path_length(first, v))
    else:
        minDist = -1
    print(dist, minDist)

from collections import defaultdict
import sys
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
INF = 10**30

class DoublingLCASeg:
    EDGE = 0

    def __init__(self, n, graph, op, e, root=0):
        self.n = n
        self.LOG = max(1, n.bit_length())
        self.op = op
        self.e = e
        self.depth = [-1] * n
        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.data = [[e] * n for _ in range(self.LOG)]

        self.depth[root] = 0
        stack = [(root, -1, e)]

        while stack:
            v, p, w = stack.pop()
            self.parent[0][v] = p
            self.data[0][v] = w

            for to, cost in graph[v]:
                if to == p:
                    continue
                self.depth[to] = self.depth[v] + 1
                stack.append((to, v, cost))

        for k in range(self.LOG - 1):
            for v in range(n):
                p = self.parent[k][v]
                if p == -1:
                    self.parent[k + 1][v] = -1
                    self.data[k + 1][v] = self.data[k][v]
                else:
                    self.parent[k + 1][v] = self.parent[k][p]
                    self.data[k + 1][v] = op(self.data[k][v], self.data[k][p])

    def kth_ancestor(self, v, k):
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    return -1
        return v

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])

        if u == v:
            return u

        for k in reversed(range(self.LOG)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]

    def prod(self, u, v):
        if u == v:
            return self.e

        op = self.op
        res = self.e

        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if diff >> k & 1:
                res = op(res, self.data[k][u])
                u = self.parent[k][u]

        if u == v:
            return res

        for k in reversed(range(self.LOG)):
            if self.parent[k][u] != self.parent[k][v]:
                res = op(res, self.data[k][u])
                res = op(res, self.data[k][v])
                u = self.parent[k][u]
                v = self.parent[k][v]

        res = op(res, self.data[0][u])
        res = op(res, self.data[0][v])
        return res


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

N = int(input())
if N == 1:
    for n in range(N-1):
        input()
    for _ in range(int(input())):
        input()
    R = int(input())
    for _ in range(R):
        input()
        print(0)
    exit(0)

ett = EulerTourTree(N)
PW = [[0, 0]]
for n in range(1, N):
    p, w = map(int, input().split())
    PW.append([p-1, w])
    ett.add_edge(n, p-1)
ett.build(root=0)
imosPlus = [0] * N
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if u == v:
        continue
    lca = ett.get_lca(u-1, v-1)
    if lca == u-1:
        imosPlus[v-1] += 1
        imosPlus[u-1] -= 1
    elif lca == v-1:
        imosPlus[u-1] += 1
        imosPlus[v-1] -= 1
    else:
        imosPlus[u-1] += 1
        imosPlus[v-1] += 1
        imosPlus[lca] -= 2

for idx in range(N-1, 0, -1):
    nxt = PW[idx][0]
    PW[idx][1] += imosPlus[idx]
    imosPlus[nxt] += imosPlus[idx]

# 最終辺重みつきグラフを作る
G = [[] for _ in range(N)]
for v in range(1, N):
    p, w = PW[v]
    G[v].append((p, w))
    G[p].append((v, w))

result = []
lca_min = DoublingLCASeg(N, G, min, INF)
R = int(input())
for _ in range(R):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        result.append(0)
    else:
        result.append(lca_min.prod(a, b))
for r in result:
    print(r)

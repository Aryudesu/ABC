from collections import defaultdict
from typing import Tuple
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

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
pos = []
for n in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))
ett = EulerTourTree(N)
for n in range(N-1):
    u, v = map(int, input().split())
    ett.add_edge(u-1, v-1)
ett.build()
ettGraph = ett.graph
treeGraph = [-1] * N
totatsu = [False] * N
nodes = {0}
while nodes:
    nextNodes = set()
    for node in nodes:
        totatsu[node] = True
        for child in ettGraph[node]:
            if totatsu[child]:
                continue
            nextNodes.add(child)
            treeGraph[child] = node
    nodes = nextNodes

def calcDist(ett: EulerTourTree, graph: list[list[int]], XY: list[Tuple[int, int]], a: int, b: int, s: int)->int:
    lca = ett.get_lca(a, b)
    nodeNum = 2
    dist = 0
    node = a
    while node != lca:
        nextNode = graph[node]
        x1, y1 = XY[node]
        x2, y2 = XY[nextNode]
        node = nextNode
        nodeNum += 1
        dist += abs(x1 - x2) + abs(y1 - y2)
    node = b
    while node != lca:
        nextNode = graph[node]
        x1, y1 = XY[node]
        x2, y2 = XY[nextNode]
        node = nextNode
        nodeNum += 1
        dist += abs(x1 - x2) + abs(y1 - y2)
    nodeNum -= 1
    return dist + S * nodeNum

result = []
S = 0
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            c = query[0]
            x, y = pos[c-1]
            pos[c-1] = (-x, -y)
        case 2:
            w = query[0]
            S += w
        case 3:
            a, b = query
            res = calcDist(ett, treeGraph, pos, a-1, b-1, S)
            result.append(res)
        case _:
            raise ValueError()
for r in result:
    print(r)

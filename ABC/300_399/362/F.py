import sys
from collections import deque

from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree

sys.setrecursionlimit(10**6)

class Tree:
    """木についてのクラス"""
    def __init__ (self, N = 1):
        self.N = N
        self.graph = dict()
        # ノードのコスト
        self.node_cost = [0] * N
        # オイラーツアーを実行したことがあるか
        self.euler_flag = False
        # 辺の長さを計算したことがあるか
        self.scn_flag = False
        self.sce_flag = False
        self.rnc_flag = False
        self.rec_flag = False
        # lcaを実行したことがあるか
        self.lca_flag = False
        # [入った時間, 出た時間]
        self.node_io = dict()
        # [ノード, 辺の重さ, 辺の重さ2, ノードの重さ, ノードの重さ2， 深さ]
        self.tour_data = []

    def set_node_cost(self, X):
        """コストを設定します"""
        assert len(X) == self.N
        self.node_cost = X

    def set_node(self, a, b, c=1):
        """aからbを繋ぐ重さcのノードを設定します"""
        tmp = self.graph.get(a, [])
        tmp.append((b, c))
        self.graph[a] = tmp

    def longest_node(self, s):
        """指定したパスから最長のパスを取得します"""
        dist = [None] * self.N
        que = deque([s])
        dist[s] = 0
        while que:
            v = que.popleft()
            d = dist[v]
            for w, c in self.graph[v]:
                if dist[w] is not None:
                    continue
                dist[w] = d + c
                que.append(w)
        d = max(dist)
        return dist.index(d), d

    def euler_tour_dfs(self, now_node):
        """オイラーツアーを行う再帰関数"""
        in_count = self.tour_count
        nodes = self.graph.get(now_node, [])
        self.node_memo[now_node] = True
        for next_node, weight in nodes:
            if self.node_memo[next_node]:
                continue
            # 行き
            self.tour_count += 1
            self.depth += 1
            self.node_memo[next_node] = True
            self.tour_data.append((now_node, weight, weight, self.node_cost[next_node], self.node_cost[next_node], self.depth))
            # 行く
            self.euler_tour_dfs(next_node)
            # 戻り
            self.tour_count += 1
            self.depth -= 1
            self.tour_data.append((now_node, 0, -weight, 0, -self.node_cost[next_node], self.depth))
            self.node_memo[next_node] = False
        out_count = self.tour_count + 1
        self.node_io[now_node] = (in_count, out_count)

    def euler_tour(self):
        """オイラーツアーを行います"""
        if self.euler_flag:
            return
        self.euler_flag = True
        first_node = 0
        self.tour_count = 0
        self.tour_weight = 0
        self.depth = 0
        self.node_memo = [False] * self.N
        self.tour_data.append((first_node, 0, 0, self.node_cost[first_node], self.node_cost[first_node], self.depth))
        self.euler_tour_dfs(first_node)
        self.tour_data.append((first_node, 0, 0, 0, -self.node_cost[first_node], self.depth))

    def depth_min(self, a, b):
        """深さが浅い方を返却します"""
        return a if a[5] < b[5] else b

    def lca(self, a, b):
        """aとbの最近共通祖先を調べます"""
        self.euler_tour()
        i_a, o_a = self.node_io.get(a, [None, None])
        i_b, o_b = self.node_io.get(b, [None, None])
        ab_max = max([i_a, o_a, i_b, o_b])
        ab_min = min([i_a, o_a, i_b, o_b])
        if not self.lca_flag:
            self.lca_segtree = SegTree(self.depth_min, (None, None, None, None, None, self.N + 1), self.tour_data)
        self.lca_flag = True
        result = self.lca_segtree.prod(ab_min, ab_max)
        return result[0]

    def subtree_cost_node(self, a):
        """aを根とする部分木のノードのコスト"""
        self.euler_tour()
        if not self.scn_flag:
            self.scn = FenwickTree(self.N * 2)
            for i in range(self.N * 2):
                self.scn.add(i, self.tour_data[i][3])
        self.scn_flag = True
        lr = self.node_io.get(a)
        return self.scn.sum(lr[0], lr[1])

    def subtree_cost_edge(self, a):
        """aを根とする部分木の辺のコスト"""
        self.euler_tour()
        if not self.sce_flag:
            self.sce = FenwickTree(self.N * 2)
            for i in range(self.N * 2):
                self.sce.add(i, self.tour_data[i][1])
        self.sce_flag = True
        lr = self.node_io.get(a)
        return self.sce.sum(lr[0] + 1, lr[1])

    def root_node_cost(self, a):
        """根からaまでのノードのコスト"""
        self.euler_tour()
        if not self.rnc_flag:
            self.rnc = FenwickTree(self.N * 2)
            for i in range(self.N * 2):
                self.rnc.add(i, self.tour_data[i][4])
        self.rnc_flag = True
        lr = self.node_io.get(a)
        return self.rnc.sum(0, lr[0] + 1)

    def root_edge_cost(self, a):
        """aを根とする部分木の辺のコスト"""
        self.euler_tour()
        if not self.rec_flag:
            self.rec = FenwickTree(self.N * 2)
            for i in range(self.N * 2):
                self.rec.add(i, self.tour_data[i][2])
        self.rec_flag = True
        lr = self.node_io.get(a)
        return self.rec.sum(0, lr[0] + 1)

    def dist_two_node_node(self, a, b):
        """aからbまでのノードの和"""
        lca = self.lca(a, b)
        return self.root_node_cost(a) + self.root_node_cost(b) - 2 * self.root_node_cost(lca) + self.node_cost[a]

    def dist_two_node_edge(self, a, b):
        """aからbまでの辺の和"""
        lca = self.lca(a, b)
        return self.root_edge_cost(a) + self.root_edge_cost(b) - 2 * self.root_edge_cost(lca)


N = int(input())
tree = Tree(N)
tree.set_node_cost([0] * N)
graph = dict()
for _ in range(N - 1):
    u, v = [int(l) - 1 for l in input().split()]
    tree.set_node(u, v)
    tree.set_node(v, u)
    tmp = graph.get(u, set())
    tmp.add(v)
    graph[u] = tmp
    tmp = graph.get(v, set())
    tmp.add(u)
    graph[v] = tmp
tree.euler_tour()
leaf = set()
all = set()
for i in range(N):
    all.add(i)
    if len(graph.get(i, set())) == 1:
        leaf.add(i)
result = []
# print("=====")
while len(all) > 1:
    # print(leaf)
    longest = -1
    x, y = None, None
    for n1 in leaf:
        for n2 in leaf:
            if n1 == n2:
                continue
            tmp = tree.dist_two_node_edge(n1, n2)
            if tmp > longest:
                longest = tmp
                x, y = n1, n2
    leaf.discard(x)
    leaf.discard(y)
    all.discard(x)
    all.discard(y)
    print(x + 1, y + 1)
    if len(all) <= 1:
        break
    nodes = graph.get(x, set())
    x2 = nodes.pop()
    graph[x] = nodes
    xnode = graph.get(x2, set())
    xnode.discard(x)
    if len(xnode) == 1:
        leaf.add(x2)
    nodes = graph.get(y, set())
    y2 = nodes.pop()
    graph[y] = nodes
    ynode = graph.get(y2, set())
    ynode.discard(y)
    if len(ynode) == 1:
        leaf.add(y2)

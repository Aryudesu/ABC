from atcoder.fenwicktree import FenwickTree
import sys
import pypyjit
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


class DFSTree:
    def __init__(self, N: int, graph: list[list[int]]):
        self.N = N
        self.graph = graph
        self.lList = [-1] * (N + 1)
        self.rList = [-1] * (N + 1)
        self.root = 1
        self.parent = [-1] * (N + 1)
        self.ft = FenwickTree(2 * N + 2)
        self.node_count = 0
        self.dfs(self.root, -1)

    def dfs(self, node: int, parent: int)->int:
        self.ft.add(self.node_count, 1)
        self.node_count += 1
        self.lList[node] = self.node_count - 1
        for nextNode in self.graph[node]:
            if nextNode == parent:
                continue
            self.parent[nextNode] = node
            self.dfs(nextNode, node)
        self.rList[node] = self.node_count - 1
        self.node_count += 1


N = int(input())
graph = [[] for _ in range(N+1)]
edge = [(-1, -1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edge.append((u, v))
dt = DFSTree(N, graph)
ft = dt.ft

allweight = N
lList = dt.lList
rList = dt.rList
parent = dt.parent

result = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        n, x, w = query
        idx = lList[x]
        allweight += w
        ft.add(idx, w)
    elif query[0] == 2:
        n, y = query
        u, v = edge[y]

        child = v if parent[v] == u else u
        lidx = lList[child]
        ridx = rList[child]
        a = ft.sum(lidx, ridx + 1)
        b = allweight - a
        result.append(abs(a-b))
    else:
        raise Exception()

for r in result:
    print(r)

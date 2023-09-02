from collections import deque, defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.parent = defaultdict(lambda: 0)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst):
        self.graph[src].append(dst)
        self.parent[dst] += 1

    def get_nodes(self):
        return self.graph.keys()


class TopologicalSort(object):
    def __init__(self, graph):
        self.g = graph.graph
        self.p = graph.parent

        self.search = defaultdict(lambda: 0)
        self.rank = defaultdict(lambda: 0)  # 順位
        self.roots = defaultdict(set)  # 各ノードの根のノード

        self.Q = deque()
        for i in self.g:
            if i not in self.p:
                self.rank[i] = 1
                self.Q.append(i)
                self.roots[i].add(i)

        while self.Q:
            queue = self.Q.pop()
            if queue not in self.g:
                continue
            for i in self.g[queue]:
                self.rank[i] = max(self.rank[i], self.rank[queue]+1)
                self.roots[i] |= self.roots[queue]
                self.search[i] += 1
                if self.search[i] == self.p[i]:
                    self.Q.append(i)

    def __repr__(self):
        return f'Node index:{self.g} rank:{self.rank} roots:{self.roots}'


N, M = map(int, input().split())
g = Graph()
for _ in range(M):
    X, Y = map(int, input().split())
    g.add_edge(X, Y)
t = TopologicalSort(g)
if len({i for i in t.rank.values()}) == N:
    print('Yes')
    ans = [0]*N
    for i in t.rank:
        ans[i-1] = t.rank[i]
    print(*ans)
else:
    print('No')

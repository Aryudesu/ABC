from collections import defaultdict


class Node:
    def __init__(self, num=0):
        self.num = num
        self.next_node = set()
        self.node_num = defaultdict(lambda: 0)
        self.dist = defaultdict(lambda: 0)
        self.data = dict()

    def add(self, to):
        self.next_node.add(to)

    def get_next(self):
        return self.next_node

    def __repr__(self):
        return f"{self.num} : {self.next_node} {self.node_num}"

class Graph:
    def __init__(self, N = 0):
        self.N = N
        self.node = dict()

    def setData(self, src, data):
        self.node.get(src, Node(src))

    def add(self, src, to):
        assert 0 <= src < self.N
        assert 0 <= to < self.N
        tmp = self.node.get(src, Node(src))
        tmp.add(to)
        self.node[src] = tmp

    def get(self, num):
        assert 0 <= node < self.N
        tmp = self.node.get(num)
        if tmp is not None:
            return tmp.get_next()
        return set()

    def draw(self):
        for num in self.node:
            print(self.node[num])

    def getGraph(self):
        return self.node

    def search_first_one(self):
        for num in self.node:
            if len(self.node[num].get_next()) == 1:
                return num

def dfs(graph: Graph, num: int, memo: set):
    next_node = graph.get(num)
    res = 0
    for node in next_node:
        if node in memo:
            continue
        memo.add(node)
        res += dfs(graph, node, memo)
        memo.discard(node)
    return res + 1


N = int(input())
graph = Graph(N)
for n in range(N-1):
    a, b = [int(l) - 1 for l in input().split()]
    graph.add(a, b)
    graph.add(b, a)
node = graph.search_first_one()
dfs(graph, node, set())


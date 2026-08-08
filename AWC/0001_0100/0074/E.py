from dataclasses import dataclass
from typing import Iterator, Tuple
from atcoder.dsu import DSU


@dataclass
class KruskalData:
    """クラスカル法で返却されるデータ"""
    nodeA: int
    nodeB: int
    cost: int
    newLeader: int

class Kruskal:
    @staticmethod
    def kruskal(n: int, edges: list[Tuple[int, int, int]])-> Iterator[KruskalData]:
        """
        クラスカル法
        @param n: ノード数
        @param edges: (コスト, ノードA, ノードB)を要素とする配列
        """
        edges = sorted(edges)
        dsu = DSU(n)
        for c, a, b in edges:
            if dsu.same(a, b):
                continue
            dsu.merge(a, b)
            yield KruskalData(a, b, c, dsu.leader(a))
    
    @staticmethod
    def kruskal_mst(n: int, edges: list[Tuple[int, int, int]])->int:
        """最小全域木のコストの総和"""
        return sum([data.cost for data in Kruskal.kruskal(n, edges)])

def getMinMax(a: int, b: int)->Tuple[int, int]:
    return min(a, b), max(a, b)

N, M = map(int, input().split())
edges = []
edgeData = set()
for m in range(M):
    u, v, w = map(int, input().split())
    u, v = getMinMax(u, v)
    edges.append((w, u-1, v-1))
    edgeData.add((w, u-1, v-1))
costData = []
for data in Kruskal.kruskal(N, edges):
    a, b = getMinMax(data.nodeA, data.nodeB)
    costData.append((data.cost, a, b))
    edgeData.discard((data.cost, a, b))
# 2つに分けてそれから繋ぎ直すのに必要なコストの最小値の最大値
print(costData)
print(edgeData)

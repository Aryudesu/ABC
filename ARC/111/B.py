from collections import defaultdict
from atcoder.dsu import DSU

class CoordinateCompress:
    def __init__(self):
        self.vals = []
        self.id = None
        self.inv = None
    
    def add(self, x)-> bool:
        """座標圧縮にデータを追加します"""
        self.vals.append(x)

    def build(self)-> None:
        """座標圧縮を行います"""
        self.inv = sorted(set(self.vals))
        self.id = {x: i for i, x in enumerate(self.inv)}

    def getId(self, data)-> int:
        """座標圧縮後のIDを取得します"""
        if data in self.id:
            return self.id[data]
        raise Exception()
    
    def getVal(self, id: int):
        """座標圧縮IDに対応するデータを取得します"""
        assert 0 <= id < len(self.inv)
        return self.inv[id]

    def __len__(self):
        return len(self.inv)

N = int(input())
cc = CoordinateCompress()
XR = []
for n in range(N):
    a, b = map(int, input().split())
    cc.add(a)
    cc.add(b)
    XR.append((a, b))
cc.build()
graph = defaultdict(list)
dsu = DSU(len(cc))
for a, b in XR:
    id1 = cc.getId(a)
    id2 = cc.getId(b)
    graph[id1].append(id2)
    graph[id2].append(id1)
    dsu.merge(id1, id2)

# 頂点の数と辺の数
memo = defaultdict(lambda:(0, 0))
for i in range(len(cc)):
    l = dsu.leader(i)
    v, e = memo[l]
    new_v, new_e = v + 1, e + len(graph[i])
    memo[l] = (new_v, new_e)
result = 0
for i in memo:
    v, e = memo[i]
    result += min(v, e//2)
print(result)

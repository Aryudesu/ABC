class CoordinateCompress:
    """座標圧縮用クラス"""
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

INF = 10 ** 18
N, M = map(int, input().split())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
cc = CoordinateCompress()
Xdata = set()
Pdata = set()
for x in X:
    cc.add(x)
    Xdata.add(x)
for p in P:
    cc.add(p)
    Pdata.add(p)
cc.build()
posData = cc.inv
L = len(posData)

isHouse = [False] * L
isHinan = [False] * L
for l in range(L):
    pos = cc.getVal(l)
    isHouse[l] = pos in Xdata
    isHinan[l] = pos in Pdata
dist = [INF] * L
prev = -INF
for l in range(L):
    pos = cc.getVal(l)
    if isHinan[l]:
        prev = pos
    dist[l] = min(dist[l], abs(prev - pos))
prev = INF
for l in range(L-1, -1, -1):
    pos = cc.getVal(l)
    if isHinan[l]:
        prev = pos
    dist[l] = min(dist[l], abs(prev - pos))
for l in range(L):
    if isHouse[l]:
        print(dist[l])

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

M, D = map(int, input().split())
cc = CoordinateCompress()
cc.add(0)
LRV = []
for m in range(M):
    l, r, v = map(int, input().split())
    LRV.append((l, r, v, m))
    cc.add(l)
    cc.add(r)

cc.build()
data = [[] for _ in range(len(cc))]
for l, r, v, m in LRV:
    lId = cc.getId(l)
    data[lId].append((-1, v, m))
    rId = cc.getId(r)
    data[rId].append((1, v, m))
zId = cc.getId(0)
# rが通り過ぎた右側
rPosSet = set()
# lが通り過ぎた左側
lPosSet = set()
s = 0
for idx in range(zId):
    for n, v, m in data[idx]:
        if n == 1:
            s += v
            rPosSet.add(m)
# print(rPosSet)
l = 0
result = -1000000000000000000
for r in range(zId, len(cc)):
    rPos = cc.getVal(r)
    for n, v, m in data[r]:
        if n == 1:
            if m not in lPosSet:
                s += v
            rPosSet.add(m)
    while l < len(cc) and min(abs(rPos), abs(cc.getVal(l))) + rPos - cc.getVal(l) > D:
        for n, v, m in data[l]:
            if n == -1:
                if m in rPosSet:
                    s -= v
                lPosSet.add(m)
        l += 1
    result = max(result, s)
print(result)

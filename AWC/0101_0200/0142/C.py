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


N, M, D, T = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Adata = set(A)
Bdata = set(B)
cc = CoordinateCompress()
cc.add(0)
cc.add(T)
for a in A:
    cc.add(a)
    cc.add(a + D)
    cc.add(a + D - 1)
for b in B:
    cc.add(b)
    cc.add(b + D)
    cc.add(b + D - 1)
cc.build()
imos = [0] * len(cc)
for a in A:
    l = cc.getId(a)
    r = cc.getId(a + D)
    imos[l] += 1
    imos[r] -= 1
for b in B:
    l = cc.getId(b)
    r = cc.getId(b + D)
    imos[l] -= 1
    imos[r] += 1
s = 0
for idx in range(len(cc)):
    s += imos[idx]
    imos[idx] = s
vals = cc.inv
# print(vals)
# print(imos)
result = 0
for idx in range(len(cc) - 1):
    if vals[idx] > T + 1:
        break
    if imos[idx] > 0:
        result += min(T + 1, vals[idx + 1]) - vals[idx]
print(result)

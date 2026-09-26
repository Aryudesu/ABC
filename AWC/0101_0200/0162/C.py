from atcoder.segtree import SegTree
from bisect import bisect_left

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
N, D = map(int, input().split())
cc = CoordinateCompress()
AC = []
for _ in range(N):
    a, c = map(int, input().split())
    AC.append((a, c))
    cc.add(a)
cc.build()
V = cc.inv
st = SegTree(min, INF, len(cc))
result = INF
data = [INF] * len(cc)
for a, c in AC:
    aId = cc.getId(a)
    if a >= D:
        result = min(result, c)
    else:
        bId = bisect_left(V, D - a)
        # print("debug", bId, len(cc))
        result = min(st.prod(bId, len(cc)) + c, result)
    st.set(aId, min(c, data[aId]))
    data[aId] = min(c, data[aId])
    # print(data)
print(result if result < INF else -1)

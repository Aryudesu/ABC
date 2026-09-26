from atcoder.segtree import SegTree

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
N, X = map(int, input().split())
cc = CoordinateCompress()
AB = dict()
for n in range(N):
    a, b = map(int, input().split())
    if a >= X:
        continue
    AB[a] = max(AB.get(a, -INF), b)
result = 0
for key, value in AB.items():
    result += max(0, value)
print(result)

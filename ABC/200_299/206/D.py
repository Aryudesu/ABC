from atcoder.dsu import DSU

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


def calc(N, A):
    cc = CoordinateCompress()
    for a in A:
        cc.add(a)
    cc.build()
    dsu = DSU(len(cc))
    i, j = 0, N - i - 1
    while i < j:
        dsu.merge(cc.getId(A[i]), cc.getId(A[j]))
        i += 1
        j -= 1
    result = 0
    for g in dsu.groups():
        result += len(g) - 1
    return result

N = int(input())
A = list(map(int, input().split()))
print(calc(N, A))

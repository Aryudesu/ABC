from atcoder.fenwicktree import FenwickTree

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

def inversion_count(arr: list) -> int:
    """転倒数を計算します"""
    result = 0
    ft = FenwickTree(max(arr) + 1)
    for i, a in enumerate(arr):
        result += i - ft.sum(0, a + 1)
        ft.add(a, 1)
    return result

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
Sset = set(S)
data = set()
for s in S:
    data.add(s)
for t in T:
    data.add(t)
data = sorted(data)
ft = FenwickTree(len(data))
cc = CoordinateCompress()
for n in range(len(data)):
    num = data[n]
    cc.add(num)
    if num not in Sset:
        ft.add(n, 1)
cc.build()
TS = []
for s, t in zip(S, T):
    TS.append((t, s))
TS.sort()
arr = []
for t, s in TS:
    arr.append(cc.getId(s))
result = inversion_count(arr)
arraft = sorted(arr)
for n in range(N):
    s, t = S[n], T[n]
    sidx = cc.getId(s)
    tidx = cc.getId(t)
    l = min(sidx, tidx) + 1
    r = max(sidx, tidx)
    result += (abs(s - t) - 1) - ft.sum(l, r) + (t not in Sset)
    # print("debug", result)
print(result)

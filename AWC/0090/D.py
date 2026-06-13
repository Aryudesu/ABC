from collections import defaultdict

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


N, B = map(int, input().split())
data = defaultdict(list)
cc = CoordinateCompress()
lrMemo = set()
result = 0
for n in range(N):
    l, r, c = map(int, input().split())
    cc.add(l)
    cc.add(r)
    data[l].append((r, B + c))
    lrMemo.add(l)
    lrMemo.add(r)
    result -= c

lrList = sorted(lrMemo)
for i in range(len(lrMemo) - 1):
    data[lrList[i]].append((lrList[i + 1], 0))
cc.build()
dp = [0] * len(cc)
for i in range(len(cc)):
    l = cc.getVal(i)
    for r, c in data[l]:
        j = cc.getId(r)
        dp[j] = max(dp[j], dp[i] + c)
result += max(dp)
print(result)

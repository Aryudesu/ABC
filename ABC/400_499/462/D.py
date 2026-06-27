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

N, D = map(int, input().split())
cc = CoordinateCompress()
times = set()
ST = []
for n in range(N):
    s, t = map(int, input().split())
    if s + D > t:
        continue
    ST.append((s, t))
    cc.add(s)
    cc.add(t-D+1)
    times.add(s)
    times.add(t-D+1)
times = sorted(set(times))
cc.build()
data = [0] * (len(cc) + 1)
for s, t in ST:
    l = cc.getId(s)
    r = cc.getId(t-D+1)
    data[l] += 1
    data[r] -= 1
sMemo = []
result = 0
s = 0
for i in range(len(cc)-1):
    s += data[i]
    if s > 0:
        tmp = (s * (s - 1)) // 2
        d = times[i+1]-times[i]
        result += tmp * d
    sMemo.append(s)
# print(times)
# print(sMemo)
print(result)

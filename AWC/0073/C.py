from bisect import bisect_left, bisect_right

class PrefixSum:
    """1次元累積和ライブラリ"""
    def __init__(self, arr: list[int]):
        self.pref = [0]
        for x in arr:
            self.pref.append(self.pref[-1] + x)

    def sum(self, l: int, r: int) -> int:
        """[l, r)の累積和を計算します"""
        return self.pref[r] - self.pref[l]

    def allSum(self) -> int:
        """全ての和を計算します"""
        return self.pref[-1]
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            l = 0 if key.start is None else key.start
            r = len(self.pref)-1 if key.stop is None else key.stop
            return self.pref[r] - self.pref[l]
        return self.pref[key]


N, D = map(int, input().split())
XS = []
for n in range(N):
    x, s = map(int, input().split())
    XS.append((x, s))
XS.sort()
sData = [s for _, s in XS]
xData = [x for x, _ in XS]
ps = PrefixSum(sData)
result = []
for idx in range(N):
    x = xData[idx]
    s = sData[idx]
    rX = x + D
    rIdx = bisect_right(xData, rX)
    res = s*ps[idx+1:rIdx]
    result.append(res)
print(sum(result))

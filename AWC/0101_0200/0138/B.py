from bisect import bisect_left

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
X = []
data = []
for n in range(N):
    x, p = map(int, input().split())
    data.append(p)
    X.append(x)
S = sum(data)
ps = PrefixSum(data)
result = 0
for idx in range(N):
    l = X[idx]
    r = l + D
    rIdx = bisect_left(X, r)
    num = ps[idx : rIdx]
    result = max(result, num)
    # print(X)
    # print(data)
    # print(idx, rIdx)
    # print(num)
print(S-result)

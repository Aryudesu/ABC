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


MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
ps = PrefixSum(A)
l = 0
r = N
s = 0
n = 1
data = [0] * N
while r - l >= 0:
    s = (s + ps[l : r]) % MOD
    data[n-1] = s
    data[-n] = s
    n += 1
    r -= 1
    l += 1
result = 0
for i in range(N):
    result = (result + data[i] * pow(i + 1, MOD-2, MOD))%MOD
print(result)

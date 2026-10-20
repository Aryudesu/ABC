# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary
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

N, M = map(int, input().split())
imos = [0] * (N + 1)
LR = []
for _ in range(M):
    l, r = map(int, input().split())
    imos[l-1] += 1
    imos[r] -= 1
    LR.append((l, r))
s = 0
count = [0] * (N + 1)
for idx in range(N):
    s += imos[idx]
    imos[idx] = 1 if s == 1 else 0
    count[idx] = 1 if s > 1 else 0
count[-1] = 0
imos[-1] = 0
ps = PrefixSum(imos)
result = sum(count) + sum(imos)
res = 10 ** 18
for l, r in LR:
    res = min(res, ps[l-1: r])
print(result - res)

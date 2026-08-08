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

N, S, K = map(int, input().split())
S -= 1
A = list(map(int, input().split()))
ps = PrefixSum(A)
result = 0
for l in range(S+1):
    if S - l > K:
        continue
    r1 = (K - (S - l))//2 + S
    r2 = S + (K - (S-l) * 2)
    result = max(result, ps[l : min(N, max(r1, r2) + 1)])
print(result)

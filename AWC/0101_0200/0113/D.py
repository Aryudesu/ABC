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


N, K = map(int, input().split())
A = list(map(int, input().split()))
ps = PrefixSum(A)
S = sum(A)
dp = [0] * (N + 1)
for idx in range(N):
    if idx + K <= N:
        dp[idx + K] = max(dp[idx + K], dp[idx] - ps[idx: idx + K])
    if idx + 1 <= N:
        dp[idx + 1] = max(dp[idx + 1], dp[idx])
print(dp[-1] + S)

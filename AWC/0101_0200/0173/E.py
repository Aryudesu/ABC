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
K = min(N-1, K)
A = list(map(int, input().split()))
ps = PrefixSum(A)
S = sum(A)
if K == 0:
    print(S)
    exit(0)
data = dict()
for k in range(K):
    data[(k, k+N-K)] = ps.sum(k, k+N-K+1) * 2
for _ in range(K-1):
    nextData = dict()
    for key, value in data.items():
        l, r = key
        if l-1 >= 0:
            nextKey = (l-1, r)
            nextData[nextKey] = max(nextData.get(nextKey, 0), (A[l-1] + value) * 2)
        if r+1 < N:
            nextKey = (l, r+1)
            nextData[nextKey] = max(nextData.get(nextKey, 0), (A[r+1] + value) * 2)
    data = nextData
print(data[(0,N-1)])

from atcoder.segtree import SegTree

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
INF = 10 ** 18
data = []
for n in range(N):
    if n + K - 1 >= N:
        break
    data.append(ps[n : n+K])
st =  SegTree(max, -INF, data)
result = 0
L = len(data)
for l in range(L):
    base = data[l]
    if l + K + 1 >= L:
        break
    # print(l, l + K + 1, L)
    nextBase = st.prod(l + K + 1, L)
    result = max(result, base + nextBase)
print(result)

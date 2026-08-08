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

H, W = map(int, input().split())
field = []
psData = []
for h in range(H):
    A = list(map(int, input().split()))
    field.append(A)
    ps = PrefixSum(A)
    psData.append(ps)
result = []
Q = int(input())
for _ in range(Q):
    r, c, d = map(int, input().split())
    r, c = r - 1, c - 1
    if d == 0:
        result.append(field[r][c])
        continue
    res = 0
    for h in range(max(0, r - d), min(H, r + d + 1)):
        l = max(0, c - abs(d - abs(r - h)))
        r = min(W, c + abs(d - abs(r - h)))
        # print("debug", h, l, r)
        res += psData[h][l:r]
    result.append(res)
print(result)


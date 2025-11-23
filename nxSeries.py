class StirlingNumber2:
    """第二種スターリング数を計算します．"""
    def __init__(self, maxN: int = 1000, mod: int = 998244353):
        self.mod = mod
        self.M = maxN
        self.data = []
        self.data.append([1])
        self._makeData()

    def _makeData(self):
        if self.M >= 1:
            self.data.append([0, 1])
        for n in range(2, self.M + 1):
            tmp = [0]
            for k in range(1, n):
                nxt = k * self.data[n-1][k] + self.data[n-1][k-1]
                if self.mod > 0:
                    tmp.append(nxt%self.mod)
                else:
                    tmp.append(nxt)
            tmp.append(1)
            self.data.append(tmp)

    def S(self, n: int, k: int):
        assert 0 <= n <= self.M
        if k < 0 or n < k:
            return 0
        return self.data[n][k]

T = 10
sn = StirlingNumber2()
frac=[1]
for n in range(1, T + 1):
    frac.append(frac[n-1] * n)
result = [1]
for t in range(1, T + 1):
    tmp = 0
    for k in range(1, t+1):
        tmp += sn.S(t, k) * 2 * frac[k]
    result.append(tmp)
print(result)

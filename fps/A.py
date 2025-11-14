class BinomialCoefficient:
    def __init__(self, n: int, mod: int=998244353):
        self.mod = mod
        self.n = n
        self.inv_data = []
        self.data = []
        self.init_data()

    def init_data(self):
        tmp = 1
        for i in range(1, self.n + 1):
            self.data.append(tmp)
            tmp = (tmp * i) % self.mod
        self.data.append(tmp)
        tmp = pow(tmp, self.mod - 2, self.mod)
        for i in range(self.n):
            self.inv_data.append(tmp)
            tmp = (tmp * (self.n - i)) % self.mod
        self.inv_data.append(tmp)
        self.inv_data.reverse()

    def calc(self, n, k):
        if n < k:
            return 0
        return (((self.data[n] * self.inv_data[n-k]) % self.mod) * self.inv_data[k]) % self.mod

D, N = map(int, input().split())
MOD = 998244353
bc = BinomialCoefficient(200005, MOD)
result = 0
for i in range(1, N - D + 1):
    if i % 2 != 0:
        continue
    if (N - D - i) % 3 != 0:
        continue
    d2 = bc.calc(D, i//2)
    d3 = bc.calc(D, (N - D - i) // 3)
    result = (result + d2 * d3) % MOD
print(result)

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
        if n < k or k < 0:
            return 0
        return (((self.data[n] * self.inv_data[n-k]) % self.mod) * self.inv_data[k]) % self.mod

N, M, S = map(int, input().split())
MOD = 998244353
bc = BinomialCoefficient(400005, MOD)
result = 0
for n in range(S+1):
    m = S - (M + 1) * n
    if S < n * (M + 1):
        break
    if m < 0:
        break
    sgn = -1 if n % 2 else 1
    result = (result + bc.calc(N, n) * bc.calc(N + m - 1, N-1) * sgn) % MOD
print(result)

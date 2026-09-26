from atcoder.dsu import DSU

def frac(N: int, mod: int = 998244353)->int:
    res = 1
    for n in range(1, N + 1):
        res *= n
        res = res % mod
    return res

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
        if k < 0:
            return 0
        if n >= 0:
            if n < k:
                return 0
            return (((self.data[n] * self.inv_data[n-k]) % self.mod) * self.inv_data[k]) % self.mod
        if n < 0:
            return self.calc(k-n-1, k) if k % 2 == 0 else -self.calc(k-n-1, k)

def S(N: int, K: int, MOD: int = 998244353)->int:
    res = pow(frac(K, MOD), MOD-2, MOD)
    bc = BinomialCoefficient(N + K)
    res2 = 0
    for i in range(K+1):
        tmp = -1 if (K - i) & 1 else 1
        tmp *= bc.calc(K, i) * pow(i, N, MOD)
        res2 = (res2 + tmp) % MOD
    return (res * res2) % MOD

MOD = 998244353
N, K, M = map(int, input().split())
dsu = DSU(K)
for m in range(M):
    u, v = map(int, input().split())
    dsu.merge(u-1, v-1)
leaders = set()
for k in range(K):
    leader = dsu.leader(k)
    leaders.add(leader)
print((frac(N) * S(len(leaders), N)) % MOD)

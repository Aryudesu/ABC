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

class RangePowerSum:
    def __init__(self, a=[], k=2, mod=998244353):
        self.N = len(a)
        self.A = a
        self.K = k
        self.MOD = mod
        self.bc = BinomialCoefficient(k, mod)

    def calc(self):
        s = 0
        data = [0] * (self.K + 1)
        result = 0
        for n in range(self.N):
            s = (s + self.A[n]) % self.MOD
            result = (result + (n + 1) * pow(s, self.K, self.MOD)) % self.MOD
            for k in range(1, self.K + 1):
                if k % 2 == 0:
                    result = (result + ((self.bc.calc(self.K, k) * pow(s, self.K - k, self.MOD)) % self.MOD) * data[k]) % self.MOD
                else:
                    result = (result - ((self.bc.calc(self.K, k) * pow(s, self.K - k, self.MOD)) % self.MOD) * data[k]) % self.MOD
            for k in range(self.K + 1):
                data[k] = (data[k] + pow(s, k, self.MOD)) % self.MOD
        return result

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
rps = RangePowerSum(A, K)
print(rps.calc())

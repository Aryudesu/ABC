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

    def calcH(self, a, b):
        return (((self.data[a+b] * self.inv_data[a]) % self.mod) * self.inv_data[b]) % self.mod

BC = BinomialCoefficient(4*(10**6) + 3)


def calc(A, B, C, D):
    mod = 998244353
    result = 0
    # b: りんごより右側にあるオレンジの数z
    for b in range(B + 1):
        tmp = BC.calcH(A-1, B - b)
        tmp = (tmp * BC.calcH(b + D, C)) % mod
        result = (result + tmp) % mod
    return result


A, B, C, D = [int(l) for l in input().split()]
result = calc(A, B, C, D)
print(result)

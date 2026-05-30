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

def calc(X1: int, X2: int, X3: int)->int:
    MOD = 998244353
    N = X1 + X2 + X3
    # 全部零ではない
    bc = BinomialCoefficient(N + 2)
    # 2を並べて間に1と3を入れていく
    result = 0
    for n in range(X2 + 2):
        # 1をn個に分割する通り数
        res1 = bc.calc(X1 - 1, n - 1)
        # 何通りの選び方があるか
        res2 = bc.calc(X2 + 1, n)
        # 残りの部分に3を入れる通り数 X3個の玉をX2 + 1 - n個の箱に入れる通り数
        res3 = bc.calc(X3 + (X2 + 1 - n) - 1, X3)
        result = (result + (res1 * res2) % MOD * res3) % MOD
    return result



X1, X2, X3 = map(int, input().split())
print(calc(X1, X2, X3))

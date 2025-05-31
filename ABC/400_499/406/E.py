MOD = 998244353
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

def calc_all(n, N, K, bc:BinomialCoefficient):
    # ある2進数でN以下の桁数でK個Bitが立っている総和を求める
    tmp = bc.calc(N-1, K-1)
    result = 0
    c = 1
    for _ in range(N):
        result = (result + c * tmp) % MOD
        c *= 2
    return (result + bc.calc(N, K) * n) % MOD

def calc(t, N, K, bc:BinomialCoefficient):
    # N以下のK個Bitが与えられる総和 + あり得る通り数 * t
    if N == 0 or K == 0:
        return t
    if N < (2**K)-1:
        return 0
    # N以下の2の冪
    n = 1
    # 桁数
    c = 0
    for i in range(61):
        if n > N:
            n//=2
            break
        c += 1
        n*=2
    # 最上位Bitが立っていない場合を考えるなら，Kはそのままで桁数を1個減らす
    result = calc_all(t, c - 1, K, bc)
    # 最上位Bitが立っている場合を考える場合はKから1を引きNからnを引く
    result = (result + calc(n + t, N - n, K - 1, bc)) % MOD
    return result

bc = BinomialCoefficient(1000)
T = int(input())
n = 1
result = []
for t in range(T):
    N, K = [int(l) for l in input().split()]
    result.append(calc(0, N, K, bc))
for r in result:
    print(r)

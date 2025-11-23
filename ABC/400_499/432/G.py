from collections import defaultdict

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

bc = BinomialCoefficient(500000)
MOD = 998244353
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Acount = defaultdict(int)
Bcount = defaultdict(int)
for a in A:
    Acount[a] += 1
for b in B:
    Bcount[b] += 1
Bset = set(B)
A = list(set(A))
B = list(Bset)
A.sort()
B.sort()
result = 0
prevA = 0
# A[i]以下でBにないデータ
bData = set()
for n in range(len(A)):
    for num in range(prevA, n + 1):
        if num in Bset:
            continue
        bData.add(num)
    prevA = n
    tmp = 0
    if len(bData) * 2 < A[n]:
        for b in bData:
            if A[n] < b:
                break
            tmp = (tmp + bc.calc(A[n], b)) % MOD
        tmp = (pow(2, A[n], MOD) - tmp) % MOD
    else:
        for m in range(len(B)):
            if A[n] < B[m]:
                break
            tmp = (tmp + bc.calc(A[n], B[m]) * Bcount[B[m]]) % MOD
    result = (result + tmp * Acount[A[n]]) % MOD
print(result)

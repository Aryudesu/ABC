from atcoder.dsu import DSU

class OsaKMethod:
    def __init__(self, n: int):
        self.spf = list(range(n))
        for p in range(2, n):
            if p * p >= n:
                break
            if self.spf[p] != p:
                continue
            for i in range(p * p, n, p):
                if self.spf[i] == i:
                    self.spf[i] = p

    def factorize(self, n: int):
        res = []
        while n > 1:
            p = self.spf[n]
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            res.append((p, c))
        return res

    def divisors(self, n: int):
        res = [1]
        for p, c in self.factorize(n):
            cur = []
            mul = 1
            for _ in range(c + 1):
                for x in res:
                    cur.append(x * mul)
                mul *= p
            res = cur
        return res

# なんでこたえあわないのおおおおおおおおおおおorz
M = 1000005
dsu = DSU(M)
osak = OsaKMethod(M)
N, K = map(int, input().split())
W = list(map(int, input().split()))
for w in W:
    D = osak.divisors(w)
    for d in D:
        if d >= K:
            dsu.merge(d, w)
data = dict()
result = 0
for w in W:
    if w < K:
        result = max(result, w)
        continue
    l = dsu.leader(w)
    tmp = data.get(l, 0) + w
    data[l] = tmp
    result = max(tmp, result)
print(result)

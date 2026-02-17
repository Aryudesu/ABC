class OsaKMethod:
    def __init__(self, n: int):
        self.n = n
        spf = list(range(n + 1))
        spf[0] = 0
        if n >= 1: spf[1] = 1
        import math
        for p in range(2, int(math.isqrt(n)) + 1):
            if spf[p] != p:
                continue
            step = p
            start = p * p
            for x in range(start, n + 1, step):
                if spf[x] == x:
                    spf[x] = p
        self.spf = spf

    def factorize(self, x: int) -> dict[int, int]:
        mp = {}
        spf = self.spf
        while x > 1:
            p = spf[x]
            c = 0
            while x > 1 and spf[x] == p:
                x //= p
                c += 1
            mp[p] = c
        return mp


def sortedInsert(data: list, num: int):
    """ソート形式で挿入"""
    tmp1, tmp2 = data
    # 最大更新
    if tmp2 <= num:
        data[0] = tmp2
        data[1] = num
        return
    # 2番目の値更新
    if tmp1 <= num:
        data[0] = num
        return


def calc(osa_k: OsaKMethod)->list[int]:
    """計算"""
    N = int(input())
    A = list(map(int, input().split()))
    expData = dict()
    soinsuData = []
    for a in A:
        peData = osa_k.factorize(a)
        soinsuData.append(peData)
        for p, e in peData.items():
            tmp = expData.get(p, [0, 0])
            sortedInsert(tmp, e)
            expData[p] = tmp
    lcm = 1
    for p, elist in expData.items():
        lcm = (lcm * pow(p, elist[-1], MOD)) % MOD
    result = []
    for i in range(N):
        factData = soinsuData[i]
        inv = 1
        for p, e in factData.items():
            lcmE = expData[p]
            if lcmE[-1] == e:
                diff = lcmE[1] - lcmE[0]
                inv_pe = pow(pow(p, diff, MOD),  MOD-2, MOD)
                inv = (inv * inv_pe) % MOD
        result.append((lcm * inv) % MOD)
    return result



MOD = 998244353
osa_k = OsaKMethod(10**7 + 10)
T = int(input())
for _ in range(T):
    res = calc(osa_k)
    print(*res)

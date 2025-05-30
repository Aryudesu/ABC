from functools import lru_cache


class OsaKMethod:
    def __init__(self, n:int = 10 ** 6):
        """下準備"""
        self.spf = list(range(n))
        for p in range(2, n):
            if p * p > n:
                break
            for i in range(p, n, p):
                if self.spf[i] == i:
                    self.spf[i] = p

    def factorize(self, n:int):
        """素因数分解"""
        if self.spf[1] == 0:
            raise Exception()
        mp = dict()
        tmp = n
        while tmp != 1:
            p = self.spf[tmp]
            mp[p] = mp.get(p, 0) + 1
            tmp //= p
        return mp

    def yakusu(self, n:int):
        """約数個数"""
        mp = self.factorize(n)
        res = 1
        for pa in mp:
            res *= (mp[pa] + 1)
        return res

    def _dfsd(self, cur_idx: int, cur_val: int, result: list, mp: list):
        """約数計算"""
        n = len(mp)
        if cur_idx == n:
            result.append(cur_val)
            return
        v = mp[cur_idx][0]
        c = mp[cur_idx][1]
        mul = 1
        for p in range(c + 1):
            self._dfsd(cur_idx + 1, cur_val * mul, result, mp)
            mul *= v
        return

    @lru_cache()
    def calc_devisors_fast(self, num:int):
        """約数列挙"""
        result = list()
        mp = self.factorize(num)
        v = list()
        for pa in mp:
            v.append([pa, mp[pa]])
        self._dfsd(0, 1, result, v)
        result.sort()
        return result




N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
osa_k = OsaKMethod()

data = dict()
yakusu = dict()
data2 = dict()
# 約数の個数調べる
for a in A:
    tmp = osa_k.calc_devisors_fast(a)
    for t in tmp:
        data[t] = data.get(t, 0) + 1
    yakusu[a] = tmp
# 約数K個以上あるやつを列挙
for a in yakusu:
    yaku = yakusu[a]
    for i in range(len(yaku)):
        y = yaku[-i-1]
        if data.get(y, 0) >= K:
            data2[a] = y
            break
for i in range(N):
    print(data2[A[i]])

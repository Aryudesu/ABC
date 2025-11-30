import math


class modQ:
    """modの有理数について Edited by Aryu"""

    # 分母の逆数をメモするための辞書
    denomMemo = dict()

    def __init__(self, numer, denom = 1, MOD = 998244353) -> None:
        """
        numer: 分子
        denom: 分母
        """
        self.MOD = MOD
        g = math.gcd(numer, denom)
        self.numer = (numer // g) % MOD
        self.denom = (denom // g) % MOD
        assert self.denom != 0

    @classmethod
    def inverseMod(cls, num, MOD):
        """逆数の計算"""
        if num in cls.denomMemo:
            return cls.denomMemo[num]
        res = pow(num, MOD-2, MOD)
        cls.denomMemo[num] = res
        return res

    def __add__(self, other):
        """加算"""
        if isinstance(other, modQ):
            new_numer = self.numer * other.denom + self.denom * other.numer
            new_denom = self.denom * other.denom
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.denom * other + self.numer
            new_denom = self.denom
            return modQ(new_numer, new_denom)
        raise Exception()

    def __radd__(self, other):
        """加算"""
        return self + other

    def __sub__(self, other):
        """減算"""
        if isinstance(other, modQ):
            new_numer = self.numer * other.denom - self.denom * other.numer
            new_denom = self.denom * other.denom
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.denom * other - self.numer
            new_denom = self.denom
            return modQ(new_numer, new_denom)
        raise Exception()

    def __rsub__(self, other):
        """減算"""
        if isinstance(other, modQ):
            new_numer = self.denom * other.numer - self.numer * other.denom
            new_denom = self.denom * other.denom
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.denom * other - self.numer
            new_denom = self.denom
            return modQ(new_numer, new_denom)
        raise Exception()


    def __mul__(self, other):
        """乗算"""
        if isinstance(other, modQ):
            new_numer = self.numer * other.numer
            new_denom = self.denom * other.denom
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.numer * other
            new_denom = self.denom
            return modQ(new_numer, new_denom)
        raise Exception()

    def __rmul__(self, other):
        """乗算"""
        return self * other

    def __floordiv__(self, other):
        """剰算"""
        if isinstance(other, modQ):
            new_numer = self.numer * other.denom
            new_denom = self.denom * other.numer
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.numer
            new_denom = self.denom * other
            return modQ(new_numer, new_denom)
        raise Exception()

    def __rfloordiv__(self, other):
        """剰算"""
        if isinstance(other, modQ):
            new_numer = other.numer * self.denom
            new_denom = other.denom * self.numer
            return modQ(new_numer, new_denom)
        elif isinstance(other, int):
            new_numer = self.denom * other
            new_denom = self.numer
            return modQ(new_numer, new_denom)
        raise Exception()

    def __iadd__(self, other):
        """ += """
        return self + other

    def __isub__(self, other):
        """ -= """
        return self - other

    def __imul__(self, other):
        """ *= """
        return self * other

    def __ifloordiv__(self, other):
        """ //= """
        return self // other

    def __pow__(self, other):
        """指数"""
        if isinstance(other, int):
            new_numer = pow(self.numer, other, self.MOD)
            new_denom = pow(self.denom, other, self.MOD)
            return modQ(new_numer, new_denom)
        raise Exception()

    def __neg__(self):
        """符号 - """
        return modQ(-self.numer, self.denom, self.MOD)

    def __pos__(self):
        """符号 + """
        return modQ(self.numer, self.denom, self.MOD)

    def __str__(self):
        """表示用"""
        inv_denom = self.inverseMod(self.denom, self.MOD)
        return str((self.numer * inv_denom) % self.MOD)

    def get_data(self):
        """分子と分母の取得"""
        return self.numer, self.denom

N = int(input())
A = list(map(int, input().split()))

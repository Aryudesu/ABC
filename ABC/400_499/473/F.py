class BucketChecker:
    """
    括弧列確認用ライブラリ
    ACLのセグ木では実行速度が気になったので移植．
    """
    def __init__(self, N: int):
        self._n = N + 1
        size = 1
        log = 0
        while size < self._n:
            size <<= 1
            log += 1
        self._size = size
        self._log = log
        self._sum = [0] * (2 * size)
        self._mn  = [0] * (2 * size)

    def _recalc(self, idx: int):
        sum_arr = self._sum
        mn_arr = self._mn
        while idx:
            l = idx << 1
            r = l | 1
            s1 = sum_arr[l]
            m1 = mn_arr[l]
            s2 = sum_arr[r]
            m2 = mn_arr[r]
            sum_arr[idx] = s1 + s2
            mn_arr[idx] = min(m1, s1 + m2)
            idx >>= 1

    def check(self, l: int, r: int) -> bool:
        """[l, r)の範囲が正しい括弧列になっているか判定します"""
        sum_arr = self._sum
        mn_arr = self._mn
        sL, mL = 0, 0
        sR, mR = 0, 0
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sx, mx = sL, mL
                sy, my = sum_arr[l], mn_arr[l]
                sL = sx + sy
                mL = min(mx, sx + my)
                l += 1
            if r & 1:
                r -= 1
                sx, mx = sum_arr[r], mn_arr[r]
                sy, my = sR, mR
                sR = sx + sy
                mR = min(mx, sx + my)
            l >>= 1
            r >>= 1
        s = sL + sR
        m = min(mL, sL + mR)
        # return s == 0 and m >= 0
        return m >= 0

    def addL(self, l: int):
        """lに(を追加します"""
        idx = l + self._size
        self._sum[idx] = 1
        self._mn[idx] = 0
        self._recalc(idx >> 1)
    
    def addR(self, r: int):
        """rに)を追加します"""
        idx = r + self._size
        self._sum[idx] = -1
        self._mn[idx] = -1
        self._recalc(idx >> 1)
    
    def add(self, l: int, r: int):
        """l, rを指定して()を追加します"""
        self.addL(l)
        self.addR(r)

N = int(input())
S = input()
bc = BucketChecker(N)
bc = BucketChecker(N)
for n in range(N):
    if S[n] == "A":
        bc.addL(n)
    else:
        bc.addR(n)

result = []
Q = int(input())
for _ in range(Q):
    n, a, b = input().split()
    n, a = int(n), int(a)
    match n:
        case 1:
            if b == "A":
                bc.addL(a-1)
            else:
                bc.addR(a-1)
        case 2:
            b = int(b)
            res = bc.check(a-1, b)
            result.append("Yes" if res else "No")
        case _:
            raise ValueError()
print(*result, sep="\n")

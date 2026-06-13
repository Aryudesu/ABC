import typing

import atcoder._bit


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> int:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        result = 0
        for i in range(1, self._log + 1):
            prev = self._d[p >> i] == 0
            res = self._update(p >> i)
            if not prev and res:
                result += 1
            elif prev and not res:
                result -= 1
        return result

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> bool:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
        return self._d[k] == 0


def op(a: int, b: int)->int:
    return a + b

N, K = map(int, input().split())
S = input()
data = []
tmp = []
for idx in range(len(S)):
    s = S[idx]
    match s:
        case "0":
            data.append(-1)
        case "1":
            data.append(1)
        case _:
            raise ValueError()

zeroNum = 0
oneNum = 0
for idx in range(K):
    s = S[idx]
    match s:
        case "0":
            zeroNum += 1
        case "1":
            oneNum += 1
        case _:
            raise ValueError()
st = SegTree(op, 0, data)
nowNum = st._d.count(0)
result = nowNum
for k in range(K):
    if k < zeroNum:
        tmp = st.set(k, -1)
    else:
        tmp = st.set(k, 1)
    nowNum += tmp
for l in range(1, N-K):
    if S[l-1] == "0":
        zeroNum -= 1
    else:
        oneNum -= 1
    if S[l + K - 1] == "0":
        zeroNum += 1
    else:
        oneNum += 1
result = max(result, nowNum)
print(result)

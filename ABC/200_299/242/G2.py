from math import isqrt


class MoLight:
    """
    Mo's Algorithm 軽量版

    クエリをMo順に並べて返す。
    add/remove等のホットループは呼び出し側に直接記述する。

    区間は半開区間 [l, r)。

    Usage:
        mo = MoLight(N, Q)

        for _ in range(Q):
            l, r = ...
            mo.addQuery(l, r)

        for l, r, qi in mo:
            while L > l:
                ...
            while R < r:
                ...
            while L < l:
                ...
            while R > r:
                ...

            ans[qi] = current
    """

    def __init__(self, N: int, Q: int):
        self.N = N
        self.Q = Q
        self.blockSize = max(1, N // max(1, isqrt(Q)))
        self.queries = []

    def addQuery(self, l: int, r: int) -> int:
        idx = len(self.queries)
        self.queries.append((l, r, idx))
        return idx

    def __iter__(self):
        B = self.blockSize

        self.queries.sort(
            key=lambda q: (
                q[0] // B,
                q[1] if (q[0] // B) & 1 == 0 else -q[1],
            )
        )

        return iter(self.queries)

N = int(input())
A = list(map(int, input().split()))

Q = int(input())

mo = MoLight(N, Q)

for _ in range(Q):
    l, r = map(int, input().split())
    mo.addQuery(l - 1, r)

cnt = [0] * (N + 1)
ans = [0] * Q

L = R = 0
pairs = 0

for l, r, qi in mo:

    while L > l:
        L -= 1
        x = A[L]
        cnt[x] += 1
        pairs += not cnt[x] & 1

    while R < r:
        x = A[R]
        cnt[x] += 1
        pairs += not cnt[x] & 1
        R += 1

    while L < l:
        x = A[L]
        cnt[x] -= 1
        pairs -= cnt[x] & 1
        L += 1

    while R > r:
        R -= 1
        x = A[R]
        cnt[x] -= 1
        pairs -= cnt[x] & 1

    ans[qi] = pairs

    ans[qi] = pairs
print(*ans, sep="\n")

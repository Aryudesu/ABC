from collections import defaultdict
from typing import Callable, Hashable


class DigitDP:
    """
    0 <= x <= n の整数 x について桁DPする汎用フレームワーク。

    状態 state は Hashable なら何でもOK。
    leading zero 中は started=False として扱う。
    """

    def __init__(self, n: int):
        self.digits = list(map(int, str(n)))

    def count(
        self,
        init_state: Hashable,
        transition: Callable[[Hashable, int, bool], Hashable | None],
        accept: Callable[[Hashable, bool], bool],
    ) -> int:
        # (state, tight, started) -> count
        dp = {(init_state, True, False): 1}

        for limit_digit in self.digits:
            ndp = defaultdict(int)

            for (state, tight, started), cnt in dp.items():
                upper = limit_digit if tight else 9

                for d in range(upper + 1):
                    ntight = tight and (d == upper)
                    nstarted = started or (d != 0)

                    nstate = transition(state, d, nstarted)
                    if nstate is None:
                        continue

                    ndp[(nstate, ntight, nstarted)] += cnt

            dp = ndp

        ans = 0
        for (state, tight, started), cnt in dp.items():
            if accept(state, started):
                ans += cnt

        return ans


# 各数字を素因数 2,3,5,7 の指数で表す
DIGIT_FACTOR = [
    (0, 0, 0, 0),  # 0: 今回は別扱い
    (0, 0, 0, 0),  # 1
    (1, 0, 0, 0),  # 2
    (0, 1, 0, 0),  # 3
    (2, 0, 0, 0),  # 4
    (0, 0, 1, 0),  # 5
    (1, 1, 0, 0),  # 6
    (0, 0, 0, 1),  # 7
    (3, 0, 0, 0),  # 8
    (0, 2, 0, 0),  # 9
]


def factorize_k(K: int):
    """K = 2^a 3^b 5^c 7^d なら (a,b,c,d)、無理なら None"""
    res = []

    for p in (2, 3, 5, 7):
        cnt = 0
        while K % p == 0:
            K //= p
            cnt += 1
        res.append(cnt)

    if K != 1:
        return None

    return tuple(res)


def count_positive_product(N: int, K: int) -> int:
    """1 <= x <= N かつ f(x) = K の個数。K > 0 を仮定。"""
    if N <= 0:
        return 0

    goal = factorize_k(K)

    # 桁 1～9 の積では作れない
    if goal is None:
        return 0

    def transition(state, digit, started):
        # まだ leading zero の途中
        if not started:
            return state

        # 数が始まった後に0が出ると積が0になる
        # 今は K > 0 なので不採用
        if digit == 0:
            return None

        e2, e3, e5, e7 = state
        d2, d3, d5, d7 = DIGIT_FACTOR[digit]

        nxt = (
            e2 + d2,
            e3 + d3,
            e5 + d5,
            e7 + d7,
        )

        # 一度goalを超えた指数は減らないので枝刈り
        if any(nxt[i] > goal[i] for i in range(4)):
            return None

        return nxt

    def accept(state, started):
        return started and state == goal

    return DigitDP(N).count(
        init_state=(0, 0, 0, 0),
        transition=transition,
        accept=accept,
    )


def count_zero_product(N: int) -> int:
    """1 <= x <= N かつ f(x) = 0 の個数。"""
    if N <= 0:
        return 0

    # state = 「実際の桁として0を使ったか」
    def transition(has_zero, digit, started):
        # leading zero は数字の0ではない
        if not started:
            return has_zero

        return has_zero or digit == 0

    def accept(has_zero, started):
        return started and has_zero

    return DigitDP(N).count(
        init_state=False,
        transition=transition,
        accept=accept,
    )


def solve(N: int, K: int) -> int:
    """1 <= x <= N で f(x) = K の個数"""
    if N <= 0:
        return 0

    if K == 0:
        return count_zero_product(N)

    return count_positive_product(N, K)


L, R, K = map(int, input().split())

print(solve(R, K) - solve(L - 1, K))
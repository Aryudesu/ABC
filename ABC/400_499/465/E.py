from collections import defaultdict
from typing import Callable, Hashable


class DigitDP:
    """
    0 <= x <= n の整数 x について桁DPする汎用フレームワーク。

    state:
        Hashable なら何でもよい。

    mod:
        None なら通常の整数で数える。
        整数を指定した場合は、その mod で答えを管理する。
    """

    def __init__(self, n: int, mod: int | None = None):
        self.digits = list(map(int, str(n)))
        self.mod = mod

    def count(
        self,
        init_state: Hashable,
        transition: Callable[[Hashable, int, bool], Hashable | None],
        accept: Callable[[Hashable, bool], bool],
    ) -> int:
        """
        transition(state, digit, started) -> next_state or None

        state:
            今までの状態

        digit:
            今置く数字

        started:
            この digit を置いた後、
            先頭ゼロを抜けて実際の数が始まっているか

        None:
            この遷移を禁止する

        accept(state, started):
            最終状態を答えに含めるか
        """

        # (state, tight, started) -> 通り数
        dp = {(init_state, True, False): 1}

        for limit_digit in self.digits:
            ndp = defaultdict(int)

            for (state, tight, started), cnt in dp.items():
                upper = limit_digit if tight else 9

                for d in range(upper + 1):
                    ntight = tight and (d == limit_digit)
                    nstarted = started or (d != 0)

                    nstate = transition(state, d, nstarted)

                    if nstate is None:
                        continue

                    key = (nstate, ntight, nstarted)
                    ndp[key] += cnt

                    if self.mod is not None:
                        ndp[key] %= self.mod

            dp = ndp

        ans = 0

        for (state, _, started), cnt in dp.items():
            if accept(state, started):
                ans += cnt

                if self.mod is not None:
                    ans %= self.mod

        return ans

OVER_NO3 = 1 << 10
OVER_HAS3 = (1 << 10) + 1
MOD = 998244353
N = int(input())

def transition(state, d, started):
    m, mask = state

    if not started:
        return state

    nm = (m + d) % 3

    if mask >= 1 << 10:
        if mask == OVER_HAS3 or d == 3:
            return nm, OVER_HAS3
        return nm, OVER_NO3

    nmask = mask | (1 << d)

    if nmask.bit_count() > 3:
        if nmask & (1 << 3):
            nmask = OVER_HAS3
        else:
            nmask = OVER_NO3

    return nm, nmask


def accept(state, started):
    if not started:
        return False
    m, mask = state
    if mask == OVER_HAS3:
        has3 = True
    elif mask == OVER_NO3:
        has3 = False
    else:
        has3 = bool(mask & (1 << 3))
    exactly3 = (
        mask < (1 << 10)
        and mask.bit_count() == 3
    )

    f = 0
    f += m == 0
    f += has3
    f += exactly3

    return f == 1


dp = DigitDP(N, MOD)
print(dp.count((0, 0), transition, accept))
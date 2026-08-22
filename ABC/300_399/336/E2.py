from collections import defaultdict
from typing import Callable, Hashable, Any


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
        """
        transition(state, digit, started) -> next_state or None
            digit: 今置く数字
            started: この digit を置いた後に正の整数として開始済みか
            None を返すと遷移不可

        accept(state, started) -> bool
            最後に数えるかどうか
        """
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


N, M = map(int, input().split())

def transition(state, d, started):
    prod = state
    if not started:
        return 1
    if d == 0:
        # 桁積 0 は今回は除外したいので、遷移自体を切ってもよい
        return None
    return (prod * d) % M

def accept(state, started):
    return started and state == 0

dp = DigitDP(N)
print(dp.count(1, transition, accept))

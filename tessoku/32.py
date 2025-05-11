import sys
from functools import lru_cache

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

def calc(turn, N, A, B, memo):
    """
    turn: 0:先手 1:後手
    N: 今の石の数
    A: 取り除ける石の数1
    B: 取り除ける石の数2
    """
    if N in memo:
        d = memo[N]
        if d[0] == turn:
            return d[1]
        return 1 - d[1]
    if N < A:
        return 1 - turn
    if calc(1 - turn, N - A, A, B, memo) == turn:
        memo[N] = (turn, turn)
        return turn
    if N >= B:
        if calc(1 - turn, N - B, A, B, memo) == turn:
            memo[N] = (turn, turn)
            return turn
    memo[N] = (turn, 1 - turn)
    return 1 - turn


N, A, B = [int(l) for l in input().split()]
res = calc(0, N, A, B, dict())
print("First" if res == 0 else "Second")

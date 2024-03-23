import sys
from functools import lru_cache

import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

@lru_cache(maxsize=1000)
def calc(N):
    if N <= 1:
        return 0
    if N % 2 == 0:
        return N + 2 * calc(N // 2)
    else:
        return N + calc(N // 2) + calc(N // 2 + 1)

N = int(input())
print(calc(N))

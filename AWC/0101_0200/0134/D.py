from typing import Tuple

def weightKeyKnapsack(items: list[Tuple[int, int]], l: int, r: int, W: int, INF: int = 10 ** 18)->int:
    """重さをキーにしてナップサック問題を計算します"""
    key = l * 500 * 500 + r * 500 + W
    if key in MEMO:
        return MEMO[key]
    NEGINF = -INF
    dp = [NEGINF] * (W + 1)
    dp[0] = 0
    result = 0
    for idx in range(l, r + 1):
        weight, value = items[idx]
        for w in range(W-weight, -1, -1):
            if dp[w] == NEGINF:continue
            dp[w + weight] = max(dp[w + weight], dp[w] + value)
            result = max(dp[w + weight], result)
    MEMO[key] = result
    return result

MEMO = dict()
N, M, Q = map(int, input().split())
items = []
for n in range(N):
    h, v = map(int, input().split())
    items.append((h, v))

for _ in range(Q):
    l, r, x = map(int, input().split())
    print(weightKeyKnapsack(items, l-1, r-1, x, M + 5))

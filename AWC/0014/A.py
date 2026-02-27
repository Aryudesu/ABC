from typing import Tuple

N, R, T = map(int, input().split())
P = list(map(int, input().split()))
result = []
for p in P:
    result.append(min(T//p, R))
print(*result)

from typing import Tuple

N, V = map(int, input().split())
D = list(map(int, input().split()))
T = list(map(int, input().split()))
result = []
s = 0
for index in range(N-1):
    d, t = D[index], T[index]
    s += d
    if s < t * V:
        result.append(index + 2)
print(*result if result else [-1])

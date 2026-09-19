from math import isqrt

N, Q = map(int, input().split())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))

memo = dict()
result = []
for _ in range(Q):
    C = int(input()) - 1
    if C in memo:
        result.append(memo[C])
        continue

    cx, cy = XY[C]
    res = 0
    for x, y in XY:
        res += isqrt((cx - x) ** 2 + (cy - y) ** 2)
    result.append(res)
    memo[C] = res
print(*result, sep="\n")

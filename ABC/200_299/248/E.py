from collections import defaultdict
from math import gcd


def getData(x1: int, y1: int, x2: int, y2: int):
    # ax + by + c = 0となる(a, b, c)を取得する
    if x1 == x2:
        return (1, 0, -x1)
    if y1 == y2:
        return (0, 1, -y1)
    dx = x1 - x2
    dy = y1 - y2
    b = dy * x1 - dx * y1
    g = gcd(gcd(abs(dx), abs(dy)), abs(b))
    if dx < 0:
        dx = -dx
        dy = -dy
        b = -b
    return (dx//g, dy//g, b//g)

def calc(XY: list[int], N: int, K: int) -> str:
    if K == 1:
        return "Infinity"
    data = defaultdict(lambda: 0)
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = getData(XY[i][0], XY[i][1], XY[j][0], XY[j][1])
            data[tmp] += 1
    K_max = (K * (K - 1))//2
    result = 0
    for k in data:
        if data[k] >= K_max:
            result += 1
    return str(result)

N, K = [int(l) for l in input().split()]
XY = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    XY.append((x, y))
print(calc(XY, N, K))

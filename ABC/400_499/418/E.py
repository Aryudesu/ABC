from math import gcd
from collections import defaultdict

class LineIdentifier:
    """2点を結ぶ直線 傾きa/bを表す(a,b)を返却する．"""

    @staticmethod
    def fromPoints(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        a = x2 - x1
        b = y2 - y1
        g = gcd(abs(a), abs(b))
        a //= g
        b //= g
        if a < 0 or (a == 0 and b < 0):
            a *= -1
            b *= -1
        return (a, b)
    
    @staticmethod
    def sqPointDist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (x2 - x1) ** 2 + (y2 - y1)**2

N = int(input())
data = defaultdict(int)
parCount = defaultdict(int)
points = [tuple([int(l) for l in input().split()]) for _ in range(N)]
plus, minus = 0, 0
for i in range(N):
    for j in range(i + 1, N):
        a, b = LineIdentifier.fromPoints(points[i], points[j])
        tmp = (a, b)
        plus += data[tmp]
        data[tmp] += 1
        dist = LineIdentifier.sqPointDist(points[i], points[j])
        tmp = (a, b, dist)
        minus += parCount[tmp]
        parCount[tmp] += 1

print(plus - minus // 2)

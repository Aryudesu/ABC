from random import randint
from math import gcd


class LineIdentifier:
    """2点を結ぶ直線 ax + by + c = 0 の(a,b,c)を返却する．"""
    @staticmethod
    def from_points(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        a = dy
        b = -dx
        c = dx * y1 - dy * x1
        g = gcd(gcd(abs(a), abs(b)), abs(c))
        a //= g
        b //= g
        c //= g
        if a < 0 or (a == 0 and b < 0):
            a *= -1
            b *= -1
            c *= -1
        return (a, b, c)

def calc(N, XY, T = 30):
    for _ in range(T):
        i = randint(0, N - 1)
        while True:
            j = randint(0, N - 1)
            if i != j:
                break
        a, b, c = LineIdentifier.from_points(XY[i], XY[j])
        count = 0
        for i in range(N):
            x, y = XY[i]
            if a * x + b * y + c == 0:
                count += 1
        if count * 2 >= N:
            return [a, b, c]
    return None

N = int(input())
XY = []
for n in range(N):
    XY.append([int(l) for l in input().split()])
result = calc(N, XY, 100)
if result is None:
    print("No")
else:
    print("Yes")
    print(*result)

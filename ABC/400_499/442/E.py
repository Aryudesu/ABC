from math import gcd, atan2

class AngleDirection:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        if x == 0 and y == 0:
            raise ValueError("Zero vector is not allowed")
        g = gcd(x, y)
        if g < 0:
            g = -g
        self.x = x // g
        self.y = y // g

    def half(self) -> int:
        return 0 if (self.y > 0 or (self.y == 0 and self.x > 0)) else 1

    def cross(self, other) -> int:
        return self.x * other.y - self.y * other.x

    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y

    def same_direction(self, other) -> bool:
        return self.cross(other) == 0 and self.dot(other) > 0

    @staticmethod
    def cmp_ccw(a, b) -> int:
        ha = a.half()
        hb = b.half()
        if ha != hb:
            return ha - hb
        c = a.cross(b)
        if c > 0:
            return -1   # a → b が反時計回り
        if c < 0:
            return 1
        return 0        # 同一直線

    def __repr__(self):
        return f"Dir({self.x}, {self.y})"

N, Q = map(int, input().split())
yxdata = []
# 直線からID
for n in range(N):
    x, y = map(int, input().split())
    g = gcd(x, y)
    if g < 0:
        g = -g
    x = x // g
    y = y // g
    at = atan2(y, x)
    if at < 0:
        at += pi * 2.0
    yxdata.append((at, y, x, n))
yxdata.sort(reverse=True)
p2Id = dict()
data = []
indexData = [None] * N
count = 0
for i in range(N):
    r, y, x, n = yxdata[i]
    if (y, x) in p2Id:
        data[p2Id[(y, x)]] += 1
    else:
        p2Id[(y, x)] = count
        data.append(1)
        count += 1
    indexData[n] = p2Id[(y, x)]
pData = [0]
l = len(data)
s = 0
for i in range(2*l):
    s += data[i%l]
    pData.append(s)
result = []
for _ in range(Q):
    a, b = map(int, input().split())
    aidx = indexData[a-1]
    bidx = indexData[b-1]
    if aidx == bidx:
        result.append(pData[bidx+1] - pData[aidx])
    else:
        if aidx > bidx:
            bidx += l
        if aidx > bidx:
            raise Exception()
        result.append(pData[bidx+1] - pData[aidx])
for r in result:
    print(r)

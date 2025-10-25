class GridSum:
    def __init__(self, H: int, W: int, field: list[list[int]]):
        self.H = H
        self.W = W
        self.field = field
        self._imosPointCount()

    def _imosPointCount(self):
        self.data = [[0] * self.W for _ in range(self.H)]
        self.data[0][0] = self.field[0][0]
        rs = self.field[0][0]
        for w in range(1, self.W):
            rs += self.field[0][w]
            self.data[0][w] = self.data[0][w-1] + rs
        for h in range(1, self.H):
            rs = 0
            for w in range(self.W):
                rs += self.field[h][w]
                self.data[h][w] = self.data[h-1][w] + rs
    
    def getNum(self, x1, y1, x2, y2):
        """左上(x1, y1)から右下(x2, y2)の矩形の内部について"""
        rx1, ry1 = min(x1, self.W), min(y1, self.H)
        rx2, ry2 = min(x2, self.W), min(y2, self.H)
        return self.data[ry2][rx2] - self.data[ry2][rx1-1] - self.data[ry1-1][rx2] + self.data[ry1-1][rx1-1]


    def debug(self):
        for dat in self.data:
            print(dat)

N = int(input())
H, W = 0, 0
XY = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    XY.append((x, y))
    W = max(x, W)
    H = max(y, H)

field = [[0] * (W + 1) for _ in range(H + 1)]
for x, y in XY:
    field[y][x] += 1

gd = GridSum(H + 1, W + 1, field)
Q = int(input())
result = []
for _ in range(Q):
    a, b, c, d = [int(l) for l in input().split()]
    result.append(gd.getNum(a, b, c, d))

for r in result:
    print(r)

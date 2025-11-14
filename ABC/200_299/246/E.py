from collections import deque, defaultdict

def xy2int(dx: int, dy: int) -> int:
    x = dx + 1
    y = (dy + 1)//2
    return x + y

def int2xy(num: int) -> list[int]:
    x = num & 2
    y = num & 1
    return [x - 1, y*2 - 1]

N = int(input())
INF = (N**2) * 2
Ax, Ay = map(int, input().split())
Ax, Ay = Ax-1, Ay-1
Bx, By = map(int, input().split())
Bx, By = Bx-1, By-1
S = [input() for _ in range(N)]
data = deque()
field = [[[INF for _ in range(4)] for _ in range(N)] for _ in range(N)]
dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for dx, dy in dir:
    field[Ax][Ay][xy2int(dx, dy)] = 0
    x2, y2 = Ax + dx, Ay + dy
    if not (0 <= x2 < N and 0 <= y2 < N):
        continue
    if S[x2][y2] != "#":
        data.append((1, x2, y2, xy2int(dx, dy)))
        field[x2][y2][xy2int(dx, dy)] = 1
while data:
    n, x, y, xy = data.popleft()
    dx, dy = int2xy(xy)
    if field[x][y][xy] < n:
        continue
    for dx2, dy2 in dir:
        x2, y2 = x + dx2, y + dy2
        if not (0 <= x2 < N and 0 <= y2 < N):
            continue
        if S[x2][y2] == "#":
            continue
        dxy2 = xy2int(dx2, dy2)
        if dx == dx2 and dy == dy2:
            if field[x2][y2][dxy2] <= n:
                continue
            data.appendleft((n, x2, y2, dxy2))
            field[x2][y2][dxy2] = n
        else:
            if field[x2][y2][dxy2] <= n + 1:
                continue
            data.append((n + 1, x2, y2, dxy2))
            field[x2][y2][dxy2] = n + 1
res = []
for dx, dy in dir:
    dxy2 = xy2int(dx, dy)
    res.append(field[Bx][By][dxy2])
r = min(res)
print(-1 if r == INF else r)

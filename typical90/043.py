from collections import deque

def dirToInt(dy: int, dx: int)-> int:
    if dy == 0 and dx == -1:
        return 0
    if dy == 0 and dx == 1:
        return 1
    if dy == -1 and dx == 0:
        return 2
    if dy == 1 and dx == 0:
        return 3

def intToDir(num: int)-> list[int, int]:
    if num == 0:
        return [0, -1]
    if num == 1:
        return [0, 1]
    if num == 2:
        return [-1, 0]
    if num == 3:
        return [1, 0]

def isSameDir(dy: int, dx: int, t: int)-> bool:
    return dirToInt(dy, dx) == t

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
H, W = map(int, input().split())
INF = H * W + 5
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
ys, xs = rs - 1, cs - 1
yg, xg = rt - 1, ct - 1

S = [input() for _ in range(H)]

field = [[[INF, INF, INF, INF] for _ in range(W)] for _ in range(H)]

# (y, x, 方向)
node = deque()
for i in range(4):
    field[ys][xs][i] = 0
    node.appendleft((ys, xs, i))

while node:
    y, x, t = node.popleft()
    prev_c = field[y][x][t]
    for dy, dx, in dirs:
        ny, nx = y + dy, x + dx
        new_c = prev_c
        new_t = dirToInt(dy, dx)
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if S[ny][nx] == "#":
            continue
        if not isSameDir(dy, dx, t):
            new_c = prev_c + 1
        if field[ny][nx][new_t] <= new_c:
            continue
        field[ny][nx][new_t] = new_c
        if new_c == prev_c:
            node.appendleft((ny, nx, new_t))
        else:
            node.append((ny, nx, new_t))

result = INF
for i in range(4):
    result = min(result, field[yg][xg][i])
print(result)

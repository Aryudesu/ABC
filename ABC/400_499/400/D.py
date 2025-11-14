from collections import deque

INF = (1000 ** 2) + 10
data = deque()
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
H, W = map(int, input().split())
S = [input() for _ in range(H)]
A, B, C, D = map(int, input().split())
A, B, C, D = A - 1, B - 1, C - 1, D - 1
fieldData = [[INF] * W for _ in range(H)]
fieldData[A][B] = 0
# (A, B)にいるときの最小手数
data.append((0, A, B))
while data:
    n, y, x = data.popleft()
    if fieldData[y][x] < n:
        continue
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        # 移動先が壁の場合
        if S[ny][nx] == "#":
            for i in range(1, 3):
                nny, nnx = y + dy * i, x + dx * i
                if 0 <= nny < H and 0 <= nnx < W:
                    if n + 1 < fieldData[nny][nnx]:
                        data.append((n + 1, nny, nnx))
                        fieldData[nny][nnx] = n + 1
        else:
            if n < fieldData[ny][nx]:
                data.appendleft((n, ny, nx))
                fieldData[ny][nx] = n
print(fieldData[C][D])

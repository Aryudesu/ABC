from collections import deque

INF = 500*500 + 5
H, W = map(int, input().split())
S = [input() for _ in range(H)]
# BFSデータ
data = deque()
data.append((0, 0, 0))
# 最小コストメモ
field = [[INF] * W for _ in range(H)]
field[0][0] = 0
# 移動方向
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while data:
    y, x, c = data.popleft()
    for dy, dx in dir:
        newy = y + dy
        newx = x + dx
        if not (0 <= newy < H):
            continue
        if not (0 <= newx < W):
            continue
        if S[newy][newx] == ".":
            if field[newy][newx] <= c:
                continue
            newc = c
            field[newy][newx] = newc
            data.appendleft((newy, newx, newc))
            continue
        if S[newy][newx] == "#":
            newc = c + 1
            if dy == 0:
                for i in range(2):
                    for j in range(3):
                        # 壊す対象
                        bx = x + dx * (i+1)
                        by = y + (j-1)
                        if not (0 <= by < H):
                            continue
                        if not (0 <= bx < W):
                            continue
                        if S[by][bx] == ".":
                            continue
                        if field[by][bx] <= newc:
                            continue
                        field[by][bx] = newc
                        data.append((by, bx, newc))
            if dx == 0:
                for i in range(2):
                    for j in range(3):
                        # 壊す対象
                        bx = x + (j-1)
                        by = y + dy * (i+1)
                        if not (0 <= by < H):
                            continue
                        if not (0 <= bx < W):
                            continue
                        if S[by][bx] == ".":
                            continue
                        if field[by][bx] <= newc:
                            continue
                        field[by][bx] = newc
                        data.append((by, bx, newc))
print(field[-1][-1])

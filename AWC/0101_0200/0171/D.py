INF = 10 ** 18
H, W = map(int, input().split())
A = []
for h in range(H):
    A.append(list(map(int, input().split())))
field = [[[INF, INF, INF, INF] for _ in range(W)] for _ in range(H)]
field[0][0][0] = 0
field[0][0][1] = 0
field[0][0][2] = 0
field[0][0][3] = 0

# 0:右, 1:左, 2:下, 3:上
node = set()
node.add((0, 0, 0))
node.add((0, 0, 1))
node.add((0, 0, 2))
node.add((0, 0, 3))
nowCount = 0
while node:
    nextNode = set()
    for y, x, c in node:
        if c == 0 or c == 1:
            if 0 <= y + 1 < H:
                ny, nx = y+1, x
                if nowCount + 1 < field[ny][nx][2] and A[ny][nx] == 0:
                    field[ny][nx][2] = min(field[ny][nx][2], nowCount + 1)
                    nextNode.add((ny, nx, 2))
            if 0 <= y - 1 < H:
                ny, nx = y-1, x
                if nowCount + 1 < field[ny][nx][3] and A[ny][nx] == 0:
                    field[ny][nx][3] = min(field[ny][nx][3], nowCount + 1)
                    nextNode.add((ny, nx, 3))
        if c == 2 or c == 3:
            if 0 <= x + 1 < W:
                ny, nx = y, x+1
                if nowCount + 1 < field[ny][nx][0] and A[ny][nx] == 0:
                    field[ny][nx][0] = min(field[ny][nx][0], nowCount + 1)
                    nextNode.add((ny, nx, 0))
            if 0 <= x - 1 < W:
                ny, nx = y, x-1
                if nowCount + 1 < field[ny][nx][1] and A[ny][nx] == 0:
                    field[ny][nx][1] = min(field[ny][nx][1], nowCount + 1)
                    nextNode.add((ny, nx, 1))
    # print(nextNode, nowCount)
    node = nextNode
    nowCount += 1
# for f in field:
#     print(f)
res = min(field[H-1][W-1])
print(res if res < INF else "NONE")

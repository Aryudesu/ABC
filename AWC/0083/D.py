from collections import deque

H, W, N = map(int, input().split())
INF = 10**18
# INF = 15
RC = [[0] * W for _ in range(H)]
for n in range(N):
    r, c = map(int, input().split())
    RC[r-1][c-1] = 1
data = deque()
data.append((0, 0, 0))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
field = [[[INF, INF, INF, INF] for _ in range(W)] for _ in range(H)]
for i in range(4):
    field[0][0][i] = 0
while data:
    y, x, n = data.popleft()
    for dn in range(4):
        dy, dx = dirs[dn]
        d = 1
        while True:
            ny, nx = y + dy * d, x + dx * d
            py, px = y + dy*(d-1), x+dx*(d-1)
            if not (0 <= ny < H):
                if d > 1 and field[py][px][dn] == n + 1:
                    data.append((py, px, n+1))
                    field[py][px][dn] = n + 1
                break
            if not (0 <= nx < W):
                if d > 1 and field[py][px][dn] == n + 1:
                    data.append((py, px, n+1))
                    field[py][px][dn] = n + 1
                break
            if RC[ny][nx] == 1:
                if d > 1 and field[py][px][dn] == n + 1:
                    data.append((py, px, n+1))
                    field[py][px][dn] = n + 1
                break
            if field[ny][nx][dn] < n + 1:
                break
            field[ny][nx][dn] = n + 1
            d += 1
res = min(field[-1][-1])
print(res if res < INF else -1)

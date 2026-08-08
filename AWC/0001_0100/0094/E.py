from heapq import heappop, heappush

H, W = map(int, input().split())
INF = H * W * 3
C = [input() for _ in range(H)]
start = None
goal = None
for h in range(H):
    for w in range(W):
        if C[h][w] == "S":
            start = (h, w)
        elif C[h][w] == "G":
            goal = (h, w)
dp = []
ny, nx = start
heappush(dp, (0, ny, nx))
result = [[INF] * W for _ in range(H)]
result[ny][nx] = 0

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while dp:
    cost, y, x = heappop(dp)
    if result[y][x] < cost:
        continue
    c = C[y][x]
    for dy, dx in dirs:
        if not (0 <= y + dy < H):
            continue
        if not (0 <= x + dx < W):
            continue
        if C[y + dy][x + dx] == "X":
            continue
        ny, nx = y + dy, x + dx
        nc = C[ny][nx]
        nextCost = cost + 1
        if nc == "V":
            if c == "V":
                nextCost = cost
            else:
                nextCost = cost + 2
        if result[ny][nx] <= nextCost:
            continue
        result[ny][nx] = nextCost
        heappush(dp, (nextCost, ny, nx))
gy, gx = goal
res = result[gy][gx]
print(res if res < INF else "NO")


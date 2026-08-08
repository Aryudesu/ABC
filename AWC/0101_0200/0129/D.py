from collections import deque

INF = 10 ** 18
H, W = map(int, input().split())
A = [input() for _ in range(H)]
field = [[INF] * W for _ in range(H)]
data = deque()
goal = None
for h in range(H):
    for w in range(W):
        a = A[h][w]
        if a == "S":
            field[h][w] = 0
            data.append((h, w))
        elif a == "G":
            goal = (h, w)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while data:
    h, w = data.popleft()
    d = field[h][w]
    for dh, dw in dirs:
        nh, nw, nd = h + dh, w + dw, d
        if not (0 <= nh < H):
            continue
        if not (0 <= nw < W):
            continue
        a = A[nh][nw]
        if a == "B":
            continue
        if a == "P":
            nd += 1
            if field[nh][nw] <= nd:
                continue
            field[nh][nw] = nd
            data.append((nh, nw))
        else:
            if field[nh][nw] <= nd:
                continue
            field[nh][nw] = nd
            data.appendleft((nh, nw))
    # for f in field:
    #     print(f)
    # print("===")

gh, gw = goal
res = field[gh][gw]
print(res if res < INF else -1)

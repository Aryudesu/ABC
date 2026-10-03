from heapq import heappop, heappush

H, W = map(int, input().split())
C = []
for h in range(H):
    c = list(map(int, input().split()))
    C.append(c)
resData = [[None] * W for _ in range(H)]
isOpen = [[False] * W for _ in range(H)]
data = []
for h in range(H):
    heappush(data, (C[h][0], h, 0))
    heappush(data, (C[h][W-1], h, W-1))
    isOpen[h][0] = True
    isOpen[h][W-1] = True
    resData[h][0] = C[h][0]
    resData[h][W-1] = C[h][W-1]
for w in range(1, W-1):
    heappush(data, (C[0][w], 0, w))
    heappush(data, (C[H-1][w], H-1, w))
    isOpen[0][w] = True
    isOpen[H-1][w] = True
    resData[0][w] = C[0][w]
    resData[H-1][w] = C[H-1][w]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
base = 0
while data:
    c, h1, w1 = heappop(data)
    base = c
    for dh, dw in dirs:
        if not (0 <= h1 + dh < H):
            continue
        if not (0 <= w1 + dw < W):
            continue
        nh, nw = h1 + dh, w1 + dw
        if isOpen[nh][nw]:
            continue
        isOpen[nh][nw] = True
        resData[nh][nw] = base + C[nh][nw]
        heappush(data, (base + C[nh][nw], nh, nw))

# for res in resData:
#     print(res)

result = []
Q = int(input())
for _ in range(Q):
    r, k = map(int, input().split())
    result.append(resData[r-1][k-1])
print(*result, sep="\n")

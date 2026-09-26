from heapq import heappush, heappop

def dist(key: tuple[int, int])->int:
    global O
    ox, oy = O
    x, y = key
    return (ox - x) ** 2 + (oy - y) ** 2

N, W, D = map(int, input().split())
O = (0, 0)
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
XY.append((0, W))
XY = sorted(XY, key=dist, reverse=True)
nodes = []
nextXY = []
for x, y in XY:
    if x == 0 and y == W:
        nextXY.append((x, y))
        continue
    if x ** 2 + y ** 2 <= D ** 2:
        heappush(nodes, (1, x, y))
    else:
        nextXY.append((x, y))
XY = nextXY
while nodes:
    n, x, y = heappop(nodes)
    O = (x, y)
    XY = sorted(XY, key=dist, reverse=True)
    # print("debug", n, x, y)
    while XY:
        nx, ny = XY.pop()
        if (x - nx) ** 2 + (y - ny) ** 2 > D**2:
            XY.append((nx, ny))
            break
        if nx == 0 and ny == W:
            print(n + 1)
            exit(0)
        heappush(nodes, (n+1, nx, ny))
print(-1)

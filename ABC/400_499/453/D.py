from typing import Tuple, Any

def xy2num(H: int, W: int, y: int, x: int)->int:
    return y * W + x

def num2xy(H: int, W: int, num: int)->Tuple[int, int]:
    return (num//W, num%W)

def getStartNGoal(H: int, W: int, S:list[str])->Tuple[Tuple[int, int]]:
    start = None
    goal = None
    for h in range(H):
        for w in range(W):
            if S[h][w] == "S":
                start = (h, w)
            elif S[h][w] == "G":
                goal = (h, w)
    return start, goal

def getResult(start: Tuple[int, int], goal: Tuple[int, int], layer: int, prevData: list[list[Tuple[Any, Any, Any, Any]]]) -> str:
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    result = []
    y, x = goal
    nl = layer
    while start != (y, x):
        py, px, pl = prevData[y][x][nl]
        dy, dx = dirs[nl]
        if dy == -1:
            result.append("U")
        elif dy == 1:
            result.append("D")
        elif dx == 1:
            result.append("R")
        elif dx == -1:
            result.append("L")
        y, x, nl = py, px, pl
    result.reverse()
    return "".join(result)

def bfs(H: int, W: int, S: list[str])->list[list[Tuple[int]]]:
    start, goal = getStartNGoal(H, W, S)
    # 移動最大値
    FMAX = H * W * 5
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    field = [[[FMAX, FMAX, FMAX, FMAX] for _ in range(W)] for _ in range(H)]
    prevData = [[[0, 1, 2, 3] for _ in range(W)] for _ in range(H)]
    sy, sx = start
    for i in range(4):
        field[sy][sx][i] = 0
        prevData[sy][sx][i] = -1
    sn = xy2num(H, W, sy, sx)
    nodes = {(sn, 0), (sn, 1), (sn, 2), (sn, 3)}
    while nodes:
        nextNodes = set()
        for node in nodes:
            pos, layer = node
            y, x = num2xy(H, W, pos)
            count = field[y][x][layer]
            nextCount = count + 1
            for nextLayer in range(4):
                dy, dx = dirs[nextLayer]
                ny = y + dy
                nx = x + dx
                if not (0 <= ny < H):
                    continue
                if not (0 <= nx < W):
                    continue
                nextPos = xy2num(H, W, ny, nx)
                if S[ny][nx] == "#":
                    continue
                if S[y][x] == "." or S[y][x] == "S" or S[y][x] == "G":
                    pass
                elif S[y][x] == "o":
                    if layer != nextLayer:
                        continue
                elif S[y][x] == "x":
                    if layer == nextLayer:
                        continue
                if field[ny][nx][nextLayer] <= nextCount:
                    continue
                field[ny][nx][nextLayer] = nextCount
                prevData[ny][nx][nextLayer] = (y, x, layer)
                nextNodes.add((nextPos, nextLayer))
                if (ny, nx) == goal:
                    return getResult(start, goal, nextLayer, prevData)
        nodes = nextNodes
    return None

H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(input())
res = bfs(H, W, S)
if res is None:
    print("No")
else:
    print("Yes")
    print(res)

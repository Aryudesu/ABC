from typing import Tuple

def makeField(N: int, C: list[str])->Tuple[Tuple[int, int], Tuple[int, int]]:
    for h in range(N):
        for w in range(N):
            if C[h][w] == "S":
                start = (h, w)
            elif C[h][w] == "G":
                goal = (h, w)
    return (start, goal)

def calc(N: int, C: list[str])->int:
    start, goal = makeField(N, C)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    memo = set()
    memo.add(start)
    result = 1
    nodes = {start}
    while nodes:
        result += 1
        nextNodes = set()
        for h, w in nodes:
            for dh, dw in dirs:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < N):
                    continue
                if not (0 <= nw < N):
                    continue
                if C[nh][nw] == "#":
                    continue
                key = (nh, nw)
                if key in memo:
                    continue
                if key == goal:
                    return result
                memo.add(key)
                nextNodes.add(key)
        nodes = nextNodes
    return -1

N = int(input())
C = [input() for _ in range(N)]
res = calc(N, C)
print(res)

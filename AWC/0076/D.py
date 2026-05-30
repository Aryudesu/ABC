from typing import Tuple

def yx2b(W: int, y: int, x: int)->int:
    return 1 << (y * W + x)

N, M, K = map(int, input().split())
Sr, Sc = map(int, input().split())
Gr, Gc = map(int, input().split())
GOALBIT = yx2b(M, Gr, Gc)


robots = 0
for k in range(K):
    p, q = map(int, input().split())
    p, q = p - 1, q - 1
    b = (1 << (p * M + q))
    robots |= b
C = [input() for _ in range(N)]

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def calcNext(H: int, W: int, nowY: int, nowX: int, nowRobots: int, next: set[Tuple[int, int, int]], memo: set[Tuple[int, int, int]])->bool:
    for dy, dx in DIRS:
        ny, nx = nowY + dy, nowX + dx
        if not (0 <= ny < H):
            continue
        if not (0 <= nx < W):
            continue
        if C[ny][nx] == "#":
            continue
        b = yx2b(W, ny, nx)
        if b & nowRobots:
            continue
        if b == GOALBIT:
            return True
        nextRobots = 0
        tmpRobots = nowRobots
        while tmpRobots:
            num = tmpRobots.bit_length()
            y = num // W
            x = num % W
    return False

node = set()
memo = set()
node.add((Sr, Sc, robots))
memo.add((Sr, Sc, robots))
while node:
    nextNodes = set()
    for nowY, nowX, nowRobots in node:
        nextData = calcNext(nowY, nowX, nowRobots)


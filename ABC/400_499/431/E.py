from collections import deque, defaultdict

INF = 10**6
def isInField(H: int, W: int, y: int, x: int) -> bool:
    return 0 <= x < W and 0 <= y < H

def calc(H: int, W: int, S:list[str])-> int:
    # (num, y, x, dy, dx) = S[y][x]にdy, dxの方向から入る このときnumの重さである
    memo = defaultdict(lambda:INF)
    data = deque([(0, 0, 0, 0, 1)])
    while data:
        n, y, x, dy, dx = data.popleft()
        if not isInField(H, W, y, x):
            continue
        costA = 1
        costB = 1
        costC = 1
        if S[y][x] == "A":
            costA = 0
        elif S[y][x] == "B":
            costB = 0
        elif S[y][x] == "C":
            costC = 0
        else:
            raise Exception()
        dyA, dxA = dy, dx
        dyB, dxB = dx, dy
        dyC, dxC = -dx, -dy
        if costA == 0:
            if n < memo[(y+dyA, x+dxA, dyA, dxA)]:
                data.appendleft((n, y+dyA, x+dxA, dyA, dxA))
                memo[(y+dyA, x+dxA, dyA, dxA)] = n
        else:
            if n + 1 < memo[(y+dyA, x+dxA, dyA, dxA)]:
                data.append((n + 1, y+dyA, x+dxA, dyA, dxA))
                memo[(y+dyA, x+dxA, dyA, dxA)] = n + 1
        if costB == 0:
            if n < memo[(y+dyB, x+dxB, dyB, dxB)]:
                data.appendleft((n, y+dyB, x+dxB, dyB, dxB))
                memo[(y+dyB, x+dxB, dyB, dxB)] = n
        else:
            if n + 1 < memo[(y+dyB, x+dxB, dyB, dxB)]:
                data.append((n + 1, y+dyB, x+dxB, dyB, dxB))
                memo[(y+dyB, x+dxB, dyB, dxB)] = n + 1
        if costC == 0:
            if n < memo[(y+dyC, x+dxC, dyC, dxC)]:
                data.appendleft((n, y+dyC, x+dxC, dyC, dxC))
                memo[(y+dyC, x+dxC, dyC, dxC)] = n
        else:
            if n + 1 < memo[(y+dyC, x+dxC, dyC, dxC)]:
                data.append((n + 1, y+dyC, x+dxC, dyC, dxC))
                memo[(y+dyC, x+dxC, dyC, dxC)] = n + 1
    return memo[(H-1, W, 0, 1)]

T = int(input())
result = []
for t in range(T):
    H, W = map(int, input().split())
    S = [input() for _ in range(H)] 
    result.append(calc(H, W, S))

for r in result:
    print(r)

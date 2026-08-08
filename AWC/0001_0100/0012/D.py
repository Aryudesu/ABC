from collections import deque

INF = 10 ** 18

def calc(N: int, M: int, S: list[str]):
    nodes = deque()
    nodes.append((0, 0))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    field = [[INF] * M for _ in range(N)]
    field[0][0] = 0
    while nodes:
        y, x = nodes.popleft()
        n = field[y][x]
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            if not (0 <= ny < N):
                continue
            if not (0 <= nx < M):
                continue
            if S[ny][nx] == "#":
                if field[ny][nx] <= n + 1:
                    continue
                field[ny][nx] = n + 1
                nodes.append((ny, nx))
            else:
                if field[ny][nx] <= n:
                    continue
                field[ny][nx] = n
                nodes.appendleft((ny, nx))
    return field[N-1][M-1]




N, M = map(int, input().split())
S = [input() for _ in range(N)]
print(calc(N, M, S))

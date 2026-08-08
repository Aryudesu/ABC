def isOk(N: int, M: int, S: list[str])->bool:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for y in range(N):
        for x in range(M):
            if S[y][x] == ".":
                continue
            c = 0
            for dy, dx in dirs:
                if not (0 <= y + dy < N):
                    continue
                if not (0 <= x + dx < M):
                    continue
                if S[y + dy][x + dx] == "#":
                    c += 1
            if not (1 <= c <= 3):
                return False
    return True

N, M = map(int, input().split())
S = [input() for _ in range(N)]
print("Yes" if isOk(N, M, S) else "No")

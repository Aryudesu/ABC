N, M = map(int, input().split())
data = set()
blks = [(0, 0), (0, 1), (1, 0), (1, 1)]
result = 0
for m in range(M):
    r, c = map(int, input().split())
    f = True
    for dr, dc in blks:
        if not (0 <= r + dr - 1 < N and 0 <= c + dc - 1 < N):
            f = False
            continue
        if (r + dr, c + dc) in data:
            f = False
            break
    if f:
        for dr, dc in blks:
            data.add((r + dr, c + dc))
        result += 1
print(result)

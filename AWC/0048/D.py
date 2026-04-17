def calcSum(y1: int, x1: int, y2: int, x2: int, field:list[list[int]])-> int:
    assert 0 <= y1 <= y2
    assert 0 <= x1 <= x2
    result = field[y2][x2]
    if y1 - 1 >= 0:
        result -= field[y1-1][x2]
    if x1 - 1 >= 0:
        result -= field[y2][x1-1]
    if y1 - 1 >= 0 and x1 - 1 >= 0:
        result += field[y1-1][x1-1]
    return result
    

def calc(H: int, W: int, K: int, field:list[list[int]])-> int:
    result = -1
    for h1 in range(H):
        for w1 in range(W):
            for h2 in range(h1, H):
                for w2 in range(w1, W):
                    if (h2 - h1 + 1) * (w2 - w1 + 1) != K:
                        continue
                    tmp = calcSum(h1, w1, h2, w2, field)
                    result = max(result, tmp)
    return result




N, M, K = map(int, input().split())
field = [[0] * M for _ in range(N)]
for n in range(N):
    S = input()
    for m in range(M):
        field[n][m] = int(S[m])
for w in range(1, M):
    field[0][w] = field[0][w-1] + field[0][w]

for h in range(1, N):
    s = field[h][0]
    field[h][0] = field[h][0] + field[h-1][0]
    for w in range(1, M):
        s += field[h][w]
        field[h][w] = s + field[h-1][w]

print(calc(N, M, K, field))

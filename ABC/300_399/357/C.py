# (y, x)にレベルKのカーペット出力
def calc(result, y, x, K):
    if K == 0:
        result[y][x] = "#"
        return
    L = 3 ** (K - 1)
    for idx1 in range(3):
        for idx2 in range(3):
            if idx1 == idx2 and idx1 == 1:
                continue
            calc(result, y + idx1 * L, x + idx2 * L, K - 1)

N = int(input())
result = [["."] * (3 ** N) for _ in range(3 ** N)]
calc(result, 0, 0, N)
for r in result:
    print("".join(r))

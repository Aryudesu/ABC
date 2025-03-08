def calc(N):
    result = [[""] * N for _ in range(N)]
    for y in range(1, N + 1):
        i = y
        j = N + 1 - i
        for y in range(i, j + 1):
            for x in range(i, j + 1):
                if i <= j:
                    if i % 2 == 1:
                        result[y - 1][x - 1] = "#"
                    else:
                        result[y - 1][x - 1] = "."
    return result

N = int(input())
res = calc(N)
for r in res:
    print("".join(r))

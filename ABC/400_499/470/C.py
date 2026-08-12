N, Q = map(int, input().split())
INF = 10 ** 6 + 5
# INF = 10
data = [0] * N
bdat = [0] * INF
bdat[0] = N
base = 0
M = 0
result = []
res = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1] - 1
            b = max(base, data[x])
            data[x] = b + 1

            bdat[b] -= 1
            bdat[b + 1] += 1
            res ^= (b - base)
            res ^= (b + 1 - base)
            M = max(M, b + 1)
        case 2:
            bdat[base + 1] += bdat[base]
            base += 1
            res = 0
            for idx in range(base, M + 1):
                if bdat[idx] % 2:
                    res ^= (idx - base)
        case _:
            raise ValueError()
    # print(data)
    # print(bdat)
    result.append(res)
print(*result, sep="\n")

N, Q = [int(l) for l in input().split()]
data = list(range(1, N + 1))
idx_start = 0
result = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, p, x = query
        data[(p - 1 + idx_start) % N] = x
    elif query[0] == 2:
        n, p = query
        result.append(data[(p - 1 + idx_start) % N])
    elif query[0]== 3:
        n, k = query
        idx_start = (idx_start + k) % N
    else:
        raise Exception()
for r in result:
    print(r)

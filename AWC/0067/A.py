N, Q = map(int, input().split())
data = [0] * N
result = []
for _ in range(Q):
    n, a, b, c = map(int, input().split())
    if n == 1:
        a, b, v = a - 1, b - 1, c
        data[a] -= v
        data[b] += v
    elif n == 2:
        x, l, r = a-1, b-1, c-1
        res = 0
        for i in range(l, r + 1):
            res += data[i] > data[x]
        result.append(res)
    elif n == 3:
        l, r, v = a-1, b-1, c
        for i in range(l, r + 1):
            data[i] += c
    else:
        raise ValueError()
for r in result:
    print(r)

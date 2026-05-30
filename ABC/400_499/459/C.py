N, Q = map(int, input().split())
base = 0
H = [N, 0]
data = [0] * N
result = []
for _ in range(Q):
    n, q = map(int, input().split())
    if n == 1:
        x = q - 1
        data[x] += 1
        h = data[x]
        if len(H) - 1 < h:
            H.append(1)
        else:
            H[h] += 1
        if len(H) > base and H[base + 1] == N:
            base += 1
    elif n == 2:
        y = q
        if len(H) - base > y:
            result.append(H[y + base])
        else:
            result.append(0)
    else:
        raise ValueError()
for r in result:
    print(r)

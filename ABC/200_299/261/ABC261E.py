N, C = [int(l) for l in input().split()]
X, Z, O = C, 0, 2**30 - 1
res = []
for n in range(N):
    t, a = [int(l) for l in input().split()]
    if t == 1:
        Z &= a
        O &= a
    elif t == 2:
        Z |= a
        O |= a
    elif t == 3:
        Z ^= a
        O ^= a
    X = (X & O) | (~X & Z)
    res.append(X)
for r in res:
    print(r)

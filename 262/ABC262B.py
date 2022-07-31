N, M = [int(l) for l in input().split()]
data = dict()
for m in range(M):
    U, V = [int(l) for l in input().split()]
    tmp = data.setdefault(U, [])
    tmp.append(V)
    data[U] = tmp
keys = data.keys()
res = 0
for a in keys:
    tmp1 = data.get(a)
    for b in tmp1:
        tmp2 = data.get(b)
        if tmp2:
            for c in tmp2:
                if c in tmp1:
                    res += 1
print(res)

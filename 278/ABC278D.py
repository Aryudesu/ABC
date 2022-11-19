N = int(input())
tmp = [int(l) for l in input().split()]
A = {idx: tmp[idx] for idx in range(N)}
base = 0
Q = int(input())
res = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        xq = query[1]
        A = dict()
        base = xq
    elif query[0] == 2:
        iq = query[1]
        xq = query[2]
        tmp = A.setdefault(iq - 1, 0)
        tmp += xq
        A[iq - 1] = tmp
    elif query[0] == 3:
        iq = query[1]
        tmp = A.get(iq-1, 0)
        res.append(base + tmp)
for r in res:
    print(r)

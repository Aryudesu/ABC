def calc(N, D, go, Num):
    dat = []
    res = []
    for i in range(N):
        dat.append([D[i], -i])
    dat.sort()
    co = 0
    if Num:
        for i in range(N):
            if go[1 - dat[-(i + 1)][1]]:
                go[1 - dat[-(i + 1)][1]] = False
                res.append(1 - dat[-(i + 1)][1])
                co += 1
                if co == Num:
                    break
    return res


N, X, Y, Z = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
go = [True] * (N + 1)
res = []
res += calc(N, A, go, X)
res += calc(N, B, go, Y)
res += calc(N, [A[i] + B[i] for i in range(N)], go, Z)
res.sort()
for r in res:
    print(r)

def calc(F, N):
    # print(F)
    BList = F[1]
    count = 0
    # 幅優先探索
    for n in range(N):
        count += 1
        NextList = []
        for l in BList:
            if N == l:
                return count
            else:
                t = F.get(l)
                if t:
                    NextList += t
        BList = NextList
    return -1



N = int(input())
P = [int(l) for l in input().split()]
F = dict()
for n in range(N-1):
    tmp = F.setdefault(P[n], [])
    tmp.append(n+2)
    F[P[n]] = tmp

print(calc(F, N))

N = int(input())
pdic = dict()
pidx = 0
narr = []
for n in range(N):
    M = int(input())
    tmp = dict()
    for m in range(M):
        p, e = [int(l) for l in input().split()]
        tmp[p] = e
        pdic[p] = 1
    narr.append(tmp)
print(narr)
print(pdic.keys())

from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
data = []
for m in range(M):
    K, C = [int(l) for l in input().split()]
    A = [int(l) - 1 for l in input().split()]
    data.append([C, K, A])
data.sort()
dsu = DSU(N)
result = 0
for C, K, A in data:
    for i in range(1, K):
        if dsu.same(A[0], A[i]):
            continue
        dsu.merge(A[0], A[i])
        result += C
print(result if len(dsu.groups()) == 1 else -1)

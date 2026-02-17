from atcoder.dsu import DSU
N = int(input())
A = [int(l) - 1 for l in input().split()]
dsu = DSU(N)
for i in range(N):
    a = A[i]
    dsu.merge(i, a)
leaders = dict()
for i in range(N):
    a = A[i]
    leader = dsu.leader(a)
    leaders[i] = leader
loops = dict()
for i in range(N):
    if A[i] == i:
        leader = leaders[i]
        loops[leader] = i
result = []
for i in range(N):
    leader = leaders[i]
    result.append(loops[leader] + 1)
print(*result)

from atcoder.dsu import DSU

N = int(input())
P = list(map(int, input().split()))
dsu = DSU(N)
for i in range(N):
    p = P[i] - 1
    # print(i, p)
    dsu.merge(i, p)
result = 0
grp = dsu.groups()
for g in grp:
    n = len(g)
    result += (n * (n-1))//2
print(result)

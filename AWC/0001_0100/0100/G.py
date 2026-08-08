from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    dsu.merge(u-1, v-1)
Q = int(input())
result = []
for _ in range(Q):
    S = int(input()) - 1
    l = dsu.leader(S)
    result.append(dsu.size(l))
for res in result:
    print(res)

from atcoder.dsu import DSU

N, M = map(int, input().split())
dsu = DSU(N)
data = [None] * N
for m in range(M):
    u, v, c = map(int, input().split())
    dsu.merge(u-1, v-1)
    leader = dsu.leader(u-1)
    data[leader] = c
colors = set()
for i in range(N):
    leader = dsu.leader(i)
    if data[leader] is None:
        continue
    colors.add(data[leader])
print(len(colors))

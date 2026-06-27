from atcoder.dsu import DSU

N, M, K = map(int, input().split())
S = list(map(int, input().split()))
dsu = DSU(N)
for m in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    dsu.merge(u, v)
leaderMemo = set()
result = 0
for s in S:
    l = dsu.leader(s - 1)
    if l in leaderMemo:
        continue
    result += dsu.size(l)
    leaderMemo.add(l)
print(result)

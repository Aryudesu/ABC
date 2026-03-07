from atcoder.dsu import DSU

MOD = 998244353
N, M = map(int, input().split())
UVC = []
for m in range(M):
    u, v = map(int, input().split())
    UVC.append((m+1, u-1, v-1))
UVC.sort(reverse=True)
dsu = DSU(N)
result = 0
leaders = set(range(N))
for c, u, v in UVC:
    ul = dsu.leader(u)
    vl = dsu.leader(v)
    if len(leaders) != 2:
        if dsu.same(u, v):
            continue
        dsu.merge(u, v)
        nl = dsu.leader(u)
        if ul == nl:
            leaders.discard(vl)
        else:
            leaders.discard(ul)
    else:
        if not dsu.same(u, v):
            result = (result + pow(2, c, MOD)) % MOD
print(result)

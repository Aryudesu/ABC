from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
AB = []
dsu = DSU(N)
loop = []
for m in range(M):
    a, b = [int(l) - 1 for l in input().split()]
    if dsu.same(a, b):
        loop.append([[a,b], m])
    dsu.merge(a, b)
data = []
leaders = set()
# print(dsu.groups())
for g in dsu.groups():
    l = dsu.leader(g[0])
    leaders.add(l)
# print(leaders)
# print(loop)
result = []
for key, num in loop:
    if len(leaders) == 1:
        break
    v = num
    k = key[0]
    kl = dsu.leader(k)
    leaders.discard(kl)
    p = leaders.pop()
    pl = dsu.leader(p)
    dsu.merge(k, p)
    nl = dsu.leader(k)
    leaders.add(nl)
    result.append([v + 1, k + 1, p + 1])
print(len(result))
for r in result:
    print(*r)

from atcoder.dsu import DSU

N, D = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
count = dict()
data = set()
dsu = DSU(10**6 + 1)
result = 0
for a in A:
    if D + a <= 10**6:
        if D + a in data:
            dsu.merge(a + D, a)
    if a - D >= 0:
        if a - D in data:
            dsu.merge(a - D, a)
    count[a] = count.get(a, 0) + 1
    data.add(a)

result = 0
if D > 0:
    gr = dsu.groups()
    for g in gr:
        if len(g) == 1:
            continue
        print(g)
        res1 = 0
        res2 = 0
        for i in range(len(g)):
            if i % 2 == 0:
                res1 += count.get(g[i], 0)
            else:
                res2 += count.get(g[i], 0)
        result += min(res1, res2)
else:
    for k in count:
        result += count[k] - 1
print(result)

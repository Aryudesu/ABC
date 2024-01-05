from atcoder.dsu import DSU

N = int(input())
dsu = DSU(N)
ones = []
for n in range(N-1):
    u, v = [int(l) - 1 for l in input().split()]
    if u == 0:
        ones.append(v)
        continue
    elif v == 0:
        ones.append(u)
        continue
    dsu.merge(u, v)
max_data = 0
for o in ones:
    max_data = max(dsu.size(o), max_data)
print(N - max_data)

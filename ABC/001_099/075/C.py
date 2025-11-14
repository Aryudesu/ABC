from atcoder.dsu import DSU

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
count = 0
for i in range(M):
    dsu = DSU(N)
    for j in range(M):
        if i == j:
            continue
        a, b = AB[j]
        dsu.merge(a-1, b-1)
    if len(dsu.groups()) == 2:
        count += 1
print(count)

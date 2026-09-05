from atcoder.dsu import DSU

N, Q = map(int, input().split())
dsu = DSU(N)
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            a, b = query
            dsu.merge(a-1, b-1)
        case 2:
            x = query[0]
            result.append(dsu.size(x-1))
        case _:
            raise ValueError()
print(*result, sep="\n")

N, Q = map(int, input().split())
V = list(map(int, input().split()))
souko = [v for v in V]
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    if n == 1:
        a, b = query
        a, b = a-1, b-1
        souko[b] += souko[a]
        souko[a] = 0
    elif n == 2:
        c = query[0]
        c = c-1
        result.append(souko[c])
    else:
        raise ValueError()

for r in result:
    print(r)

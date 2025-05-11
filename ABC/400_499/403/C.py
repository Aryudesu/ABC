from collections import defaultdict

data = defaultdict(set)
N, M, Q = [int(l) for l in input().split()]
result = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, x, y = query
        data[x].add(y)
    elif query[0] == 2:
        n, x = query
        data[x].add(-1)
    elif query[0] == 3:
        n, x, y = query
        if y in data[x] or -1 in data[x]:
            result.append("Yes")
        else:
            result.append("No")
    else:
        raise Exception()
for r in result:
    print(r)

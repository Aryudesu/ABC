N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = []
np = -1
data = dict()
for a in A:
    tmp = data.get(a, 0) + 1
    if data.get(np, 0) < tmp:
        np = a
    elif data.get(np, 0) == tmp:
        if np > a:
            np = a
    data[a] = tmp
    result.append(np)
for r in result:
    print(r)

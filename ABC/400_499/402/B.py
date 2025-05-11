Q = int(input())
result = []
idx = 0
data = []
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        a, x = query
        data.append(x)
    elif query[0] == 2:
        result.append(data[idx])
        idx += 1
    else:
        raise Exception()
for r in result:
    print(r)

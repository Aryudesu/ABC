Q = int(input())
bag = dict()
data = set()
result = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    q = int(query[0])
    if q == 1:
        x = int(query[1])
        bag[x] = bag.get(x, 0) + 1
        data.add(x)
    elif q == 2:
        x = int(query[1])
        bag[x] = bag.get(x, 0) - 1
        if bag[x] == 0:
            data.discard(x)
    elif q == 3:
        result.append(len(data))
for r in result:
    print(r)

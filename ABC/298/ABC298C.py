import bisect


N = int(input())
Q = int(input())
data = dict()
bc_data = dict()
b_data = dict()
result = []
for q in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        tmp = data.get(query[2], [])
        bisect.insort(tmp, query[1])
        data[query[2]] = tmp

        bc = bc_data.get(query[1], set([]))
        if not query[2] in bc:
            tmp = b_data.get(query[1], [])
            bisect.insort(tmp, query[2])
            b_data[query[1]] = tmp

            bc.add(query[2])
            bc_data[query[1]] = bc
    elif query[0] == 2:
        tmp = data.get(query[1], [])
        print(*tmp)
    elif query[0] == 3:
        tmp = b_data.get(query[1], [])
        print(*tmp)

Q = int(input())
A = []
result = []
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        q, x = query
        A.append(x)
    elif query[0] == 2:
        q, k = query
        result.append(A[-k])
for r in result:
    print(r)

N, Q = [int(l) for l in input().split()]
A = [l + 1 for l in range(N)]
result = []
rev = False
for q in range(Q):
    num, *query = [int(l) for l in input().split()]
    if num == 1:
        x, y = query
        x -= 1
        if rev:
            x = - x - 1
        A[x] = y
    elif num == 2:
        rev = not rev
    elif num == 3:
        x = query[0]
        x -= 1
        if rev:
            x = - x - 1
        result.append(A[x])
for r in result:
    print(r)

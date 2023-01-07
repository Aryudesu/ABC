N = int(input())
A = [int(l) for l in input().split()]
Q = int(input())
res = []
for q in range(Q):
    Query = [int(l) for l in input().split()]
    if Query[0] == 1:
        A[Query[1] - 1] = Query[2]
    elif Query[0] == 2:
        res.append(A[Query[1] - 1])
for r in res:
    print(r)

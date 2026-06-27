N, C, Q = map(int, input().split())
A = list(map(int, input().split()))
result = []
for _ in range(Q):
    n, *query = map(int, input().split())
    match n:
        case 1:
            p, x = query
        case 2:
            l, r, d = query
            l, r = l-1, r-1
        case _:
            raise ValueError()
for r in result:
    print(r)

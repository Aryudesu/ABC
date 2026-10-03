N, Q = map(int, input().split())
A = []
B = [0]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.append(0)
for _ in range(Q):
    num, *query = map(int, input().split())
    match num:
        case 1:
            i, a, b = query
        case 2:
            s = query[0]

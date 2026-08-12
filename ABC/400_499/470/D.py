N, Q = map(int, input().split())
P = [int(l) - 1 for l in input().split()]
# print(P)
P2 = [None] * N
for i in range(N):
    P2[P[i]] = i
result = []
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x, y = query[1] - 1, query[2] - 1
            l, r = P[x], P[y]
            P[x], P[y] = P[y], P[x]
            P2[l], P2[r] = P2[r], P2[l]
        case 2:
            P, P2 = P2, P
        case _:
            raise ValueError()
display = [p + 1 for p in P]
print(*display)

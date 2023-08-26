N, M = [int(l) for l in input().split()]
P = [True] * (N+1)
P[0] = False
for m in range(M):
    a, b = [int(l) for l in input().split()]
    P[b] = False
if P.count(True) == 1:
    print(P.index(True))
else:
    print(-1)

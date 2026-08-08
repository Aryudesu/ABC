N, L, R, T = map(int, input().split())
PS = []
for n in range(N):
    p, s = map(int, input().split())
    if s >= T and L <= p <= R:
        PS.append((p, -s, n))
if len(PS) == 0:
    print(-1)
else:
    PS.sort()
    print(PS[0][2] + 1)

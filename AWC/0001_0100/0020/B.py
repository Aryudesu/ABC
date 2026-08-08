N, M, S = map(int, input().split())
D = list(map(int, input().split()))
bate = False
yamagoya = dict()
for m in range(M):
    p, r = map(int, input().split())
    yamagoya[p-1] = r
for n in range(N):
    if bate:
        S -= 2 * D[n]
    else:
        S -= D[n]
    if S <= 0:
        bate = True
    if n in yamagoya:
        S += yamagoya[n]
print(S)

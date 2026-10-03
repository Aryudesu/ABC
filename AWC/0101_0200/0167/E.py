N, M, K = map(int, input().split())
minW = 10**18
for m in range(M):
    u, v, w = map(int, input().split())
    minW = min(minW, w)
print(minW)

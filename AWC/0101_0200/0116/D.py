N, M = map(int, input().split())
WT = []
for _ in range(N):
    W, T = map(int, input().split())
    WT.append((W, T))
WT.sort()
P = []
for _ in range(M):
    P.append(int(input()))


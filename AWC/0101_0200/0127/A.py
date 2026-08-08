N, K = map(int, input().split())
S = list(map(int, input().split()))
T = [s for s in S if s >= K]
if T:
    print(sum(T)/len(T))
else:
    print(-1)

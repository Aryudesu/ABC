N, K = map(int, input().split())
S = list(map(int, input().split()))
print(sum(1 if s >= K else 0 for s in S))

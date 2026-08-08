N, K = map(int, input().split())
P = list(map(int, input().split()))
print(sum(p for p in P if p >= K))

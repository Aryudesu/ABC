N, W = map(int, input().split())
V = list(map(int, input().split()))
for v in V:
    if v <= W:
        W += v
print(W)

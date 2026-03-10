N, D, K = map(int, input().split())
W = list(map(int, input().split()))
print(sum(w - D * K >= 1 for w in W))

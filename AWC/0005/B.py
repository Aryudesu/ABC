N, M, K = map(int, input().split())
S = list(map(int, input().split()))
for m in range(M):
    p, v = map(int, input().split())
    S[p-1] = v
result = 0
for s in S:
    if s < K:
        result += 1
print(result)

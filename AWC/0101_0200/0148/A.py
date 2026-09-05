N, D, K = map(int, input().split())
data = [0] * (N + 1)
for d in range(D):
    M, *S = map(int, input().split())
    for s in S:
        data[s] += 1
result = []
for idx in range(1, N + 1):
    if data[idx] >= K:
        result.append(idx)
if result:
    print(*result)
else:
    print(-1)

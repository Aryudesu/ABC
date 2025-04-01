from collections import defaultdict

N = int(input())
P = [int(l) for l in input().split()]
data = []
for idx in range(N):
    p = P[idx]
    data.append((p, idx + 1))
data.sort(reverse=True)
result = defaultdict(lambda: N + 1)
for idx in range(N):
    score = data[idx][0]
    result[score] = min(idx + 1, result[score])
for p in P:
    print(result[p])

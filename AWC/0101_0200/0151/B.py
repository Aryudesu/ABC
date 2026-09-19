from collections import defaultdict
N, M = map(int, input().split())
P = list(map(int, input().split()))
data = defaultdict(int)
taka = 0
M = 0
result = 0
for p in P:
    data[p] += 1
    M = max(M, data[p])
    if p == 2:
        if data[p] < M:
            result += 1
print(result)

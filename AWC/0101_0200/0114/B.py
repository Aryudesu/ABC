from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = set()
data = defaultdict(set)
for idx in range(N):
    data[A[idx]].add(idx)

for key in data:
    if K != 0:
        if key + K in data:
            result.update(data[key + K])
            result.update(data[key])
        if key - K in data:
            result.update(data[key - K])
            result.update(data[key])
    else:
        if len(data[key]) > 1:
            result.update(data[key])
print(len(result))

from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))

data = defaultdict(int)
result = 0
for a in A:
    if K-a in data:
        result += data[K-a]
    data[a] += 1
print(result)

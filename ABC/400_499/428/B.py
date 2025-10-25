from collections import defaultdict

N, K = [int(l) for l in input().split()]
S = input()
data = defaultdict(int)
maxCount = 0
for i in range(N-K+1):
    tmp = S[i:i+K]
    data[tmp] += 1
    maxCount = max(maxCount, data[tmp])
result = []
for key in data:
    if data[key] == maxCount:
        result.append(key)
result.sort()
print(maxCount)
print(" ".join(result))

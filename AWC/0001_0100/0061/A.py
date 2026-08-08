from collections import defaultdict

N, M = map(int, input().split())
data = defaultdict(int)
for n in range(N):
    K, *C = list(map(int, input().split()))
    for c in C:
        data[c] += 1
result = 0
for key, num in data.items():
    if num == N:
        result += 1
print(result)

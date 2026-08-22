from collections import defaultdict

N = int(input())
data = defaultdict(int)
for n in range(N):
    S = input().lower()
    data[S] += 1
result = 0
for key, value in data.items():
    result = max(value, result)
print(result)

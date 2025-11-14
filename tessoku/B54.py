from collections import defaultdict
N = int(input())
data = defaultdict(int)
for n in range(N):
    data[int(input())] += 1
result = 0
for k in data:
    result += data[k] * (data[k] - 1) // 2
print(result)

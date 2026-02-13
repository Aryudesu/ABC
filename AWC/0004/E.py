from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = [0]
s = 0
for a in A:
    s += a
    data.append(s)
# print(data)
result = 0
memo = defaultdict(int)
for idx in range(len(data)):
    result += memo[data[idx] - K]
    memo[data[idx]] += 1
print(result)

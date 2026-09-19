from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
data = defaultdict(int)
for n in range(N):
    result += data[A[n] - K]
    result += data[A[n] + K]
    data[A[n]] += 1
print(result)

N = int(input())
V = list(map(int, input().split()))
P = [-1]
if N > 1:
    P = [-1] + list(map(int, input().split()))
data = V.copy()
for idx in range(N-1, 0, -1):
    data[P[idx]-1] += data[idx]
result = data[0]
for idx in range(1, N):
    result = min(result, result - data[idx])
print(result)

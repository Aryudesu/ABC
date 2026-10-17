N, K = map(int, input().split())
C = list(map(int, input().split()))
P = [0] + list(map(int, input().split()))
A = set(map(int, input().split()))
result = [0] * N
for idx in range(N-1, 0, -1):
    if idx + 1 in A or result[idx]:
        result[idx] += C[idx]
    result[P[idx]-1] += result[idx]
if result[0] or 1 in A:
    result[0] += C[0]
print(result[0])

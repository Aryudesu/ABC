N, K = map(int, input().split())
A = list(map(int, input().split()))
s = 0
for idx in range(K):
    s += A[idx]
result = 1 if s <= 0 else 0
for i in range(N-K):
    s -= A[i]
    s += A[i + K]
    result += 1 if s <= 0 else 0
print(result)

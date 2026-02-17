N, K = map(int, input().split())
A = list(map(int, input().split()))
m = -1
res = -1
for i in range(N):
    if A[i] > m:
        m = A[i]
        res = i + 1
print(res)

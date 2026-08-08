N = int(input())
A = list(map(int, input().split()))
result = list(range(N))
for i in range(1, N):
    if A[i-1] <= A[i]:
        result[i] = 0
print(*result)

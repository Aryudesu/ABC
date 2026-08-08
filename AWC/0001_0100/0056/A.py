N, M = map(int, input().split())
A = list(map(int, input().split()))
result = 0
for _ in range(M):
    b, s = map(int, input().split())
    result += A[b-1] + s
print(result)

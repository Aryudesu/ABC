N, M = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(M):
    b, c = map(int, input().split())
    b -= 1
    if A[b] >= c:
        A[b] -= c
print(*A)

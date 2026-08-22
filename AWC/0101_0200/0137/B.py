N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
result = []
for _ in range(Q):
    x, y = map(int, input().split())
    S += y - A[x-1] 
    A[x-1] = y
    result.append(S)
print(*result, sep = "\n")

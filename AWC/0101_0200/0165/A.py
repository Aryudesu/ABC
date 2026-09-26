N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
for c in C:
    if c < N:
        A[c] += max(0, A[c-1] - B[c-1])
    A[c-1] = 0
print(*A)

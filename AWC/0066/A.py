N, Q = map(int, input().split())
A = list(map(int, input().split()))
Bdata = set()
for _ in range(Q):
    b = int(input()) - 1
    a = A[b]
    A[b] = 0
    if b + 1 < N:
        A[b + 1] += a
print(*A)

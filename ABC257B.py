N, K, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
L = [int(l) for l in input().split()]
B = [0 for l in range(N)]

for a in range(len(A)):
    B[A[a]-1] = a+1

for l in range(len(L)):
    idx = L[l]
    a = A[idx - 1]
    if a != N:
        if not B[a]:
            B[a], B[a-1] = B[a-1], 0
            A[idx-1] = a+1
print(*A)

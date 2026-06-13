N, Q = map(int, input().split())
A = list(map(int, input().split()))
res = sum(A)
for _ in range(Q):
    D = int(input())
    res -= A[D-1]
    A[D-1] = 0
    print(res)

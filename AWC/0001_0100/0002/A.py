N, K = map(int, input().split())
A = [-10000000] + list(map(int, input().split()))
if K in A:
    print(A.index(K))
else:
    print(-1)

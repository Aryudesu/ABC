N = int(input())
A = list(map(int, input().split()))
M = max(A)
if A.count(M) > 1:
    print(-1)
else:
    print(A.index(M) + 1)

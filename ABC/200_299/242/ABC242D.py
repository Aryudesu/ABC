from sortedcontainers import SortedList

Q = int(input())
A = SortedList()
res = []
for _ in range(Q):
    n, *query = list(map(int, input().split()))
    if n == 1:
        x = query[0]
        A.add(x)
    elif n == 2:
        x, k = query
        idx= A.bisect_right(x) - 1
        if idx + 1 >= k:
            print(A[idx - k + 1])
        else:
            print(-1)
    elif n == 3:
        x, k = query
        idx = A.bisect_left(x)
        if len(A) > idx + k - 1:
            print(A[idx + k - 1])
        else:
            print(-1)


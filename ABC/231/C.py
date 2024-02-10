from bisect import bisect_left

N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
result = []
for q in range(Q):
    x = int(input())
    tmp = bisect_left(A, x)
    result.append(N - tmp)
for r in result:
    print(r)

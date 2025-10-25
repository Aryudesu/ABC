from bisect import bisect_left

N = int(input())
A = [int(l) for l in input().split()]
A.sort()
result = []
Q = int(input())
for q in range(Q):
    x = int(input())
    idx = bisect_left(A,x)
    result.append(idx)
for r in result:
    print(r)

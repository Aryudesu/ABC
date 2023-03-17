import bisect

N, X = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(bisect.bisect_left(A, X) + 1)

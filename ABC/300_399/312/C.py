import bisect

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort()
B.sort()
C = list(set(A) | set(B))
C.sort()
for c in C:
    pass

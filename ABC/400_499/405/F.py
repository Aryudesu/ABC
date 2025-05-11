from collections import defaultdict

from sortedcontainers import SortedSet

N, M = [int(l) for l in input().split()]
data = defaultdict(SortedSet)
for m in range(M):
    A, B = [int(l) for l in input().split()]
    A, B = min(A, B), max(A, B)
    data[A].add(B)
    data[B].add(A)
Q = int(input())
for _ in range(Q):
    C, D = [int(l) for l in input().split()]
    C, D = min(C, D), max(C, D)
    if (D - C) * 2 >= N:
        pass
print(data)

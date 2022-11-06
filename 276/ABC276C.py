import itertools
N = int(input())
P = tuple(int(l) for l in input().split())
L = [l for l in range(1, N+1)]
A = list(itertools.permutations(L))
idx = (A.index(P))
print(*A[idx-1])

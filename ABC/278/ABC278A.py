N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()] + [0] * K
print(*A[K:])

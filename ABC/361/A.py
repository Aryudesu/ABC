N, K, X = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = A[:K] + [X] + A[K:]
print(*B)

N, M, B = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
print(sum(A) * M + sum(C) * N + B * N * M)

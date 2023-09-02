N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
result = 0
for m in range(M):
    result += A[B[m] - 1]
print(result)

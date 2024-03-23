N = int(input())
A = [int(l) for l in input().split()]
B = []
for n in range(N-1):
    B.append(A[n] * A[n + 1])
print(*B)

N = int(input())
A = [int(l) for l in input().split()]
S = sum(A)
result = 0
for n in range(N):
    result += (A[n] ** 2) * (N - 1)

for n in range(N):
    S -= A[n]
    result -= 2 * A[n] * S

print(result)

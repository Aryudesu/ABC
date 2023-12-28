N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
result = 0
for n in range(N):
    result += A[n] / 3 + B[n] * 2 / 3
print(result)

N = int(input())
A = [int(l) for l in input().split()]
result = 0
for i in range(N):
    if i % 2 == 0:
        result += A[i]
print(result)


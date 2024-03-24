N = int(input())
A = [int(l) for l in input().split()]
A.sort(reverse=True)
result = 0
for i in range(N):
    result += (-1)**i * A[i]
print(result)

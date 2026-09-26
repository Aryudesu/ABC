N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
result = 0
for i in range(N):
    if i % 2:
        continue
    result += A[i]
print(result)

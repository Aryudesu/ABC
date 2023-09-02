N = int(input())
A = [int(l) for l in input().split()]
result = []
for n in range(N):
    s = 0
    for i in range(7):
        s += A[n*7 + i]
    result.append(s)
print(*result)

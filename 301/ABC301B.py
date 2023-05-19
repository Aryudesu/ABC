N = int(input())
A = [int(l) for l in input().split()]
idx = 0
num = A[0]
result = [A[0]]
for i in range(N-1):
    diff = A[i + 1] - A[i]
    if abs(diff) != 1:
        d = 1 if diff > 0 else -1
        while abs(diff) != abs(d):
            result.append(A[i] + d)
            if diff > 0:
                d += 1
            else:
                d -= 1
    result.append(A[i + 1])
print(*result)

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
l = 0
r = N - 1
result = 0
for n in range(N):
    if A[n] - A[0] > K:
        r = n
        break
for n in range(N):
    for m in range(N):
        if r + m >= N:
            r = r + m
            break
        if A[n] - A[r + m] > K:
            r = r + m
            break
    result += r - n - 1
print(result)

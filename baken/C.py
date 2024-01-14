N, M = [int(l) for l in input().split()]
A = []
for n in range(N):
    A.append([int(l) for l in input().split()])

result = 0
for t1 in range(M):
    for t2 in range(M):
        if t1 == t2:
            break
        tmp = 0
        for n in range(N):
            tmp += max(A[n][t1], A[n][t2])
        result = max(tmp, result)
print(result)


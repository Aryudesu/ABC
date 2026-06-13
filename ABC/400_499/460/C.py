N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
aIdx = 0
result = 0
for bIdx in range(M):
    while aIdx < N and B[bIdx] > A[aIdx] * 2:
        aIdx += 1
    if aIdx >= N:
        break
    if B[bIdx] <= A[aIdx] * 2:
        result += 1
        aIdx += 1
    if aIdx >= N:
        break
print(result)

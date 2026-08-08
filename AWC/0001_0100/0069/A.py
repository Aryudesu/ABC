N, M = map(int, input().split())
maxIdx = 0
maxNum = 0
for n in range(N):
    A = list(map(int, input().split()))
    s = 0
    for m in range(1, M):
        s += abs(A[m] - A[m-1])
    if s > maxNum:
        maxIdx = n
        maxNum = s
print(maxIdx + 1)

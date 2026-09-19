N, M = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
A.sort()
L.sort()
lIdx = 0
count = 0
for idx in range(1, N):
    sa = A[0] + A[idx]
    while lIdx < M and L[lIdx] < sa:
        lIdx += 1
    if lIdx >= M:
        break
    count += 1
    lIdx += 1
print("Yes" if count + 1 == N else "No")

from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bs = SortedList(B)
aset = SortedList(A)
result = 0
count = 0
for n in range(N):
    a = A[n]
    if a in bs:
        bs.discard(a)
        aset.discard(a)
        count += 1
        result += 1
A = aset
B = bs
isOk = True
aIdx = 0
for bIdx in range(len(B)):
    while aIdx < len(aset):
        a = A[aIdx]
        if B[bIdx] <= a:
            count += 1
            result += B[bIdx] == a
            aIdx += 1
            break
        aIdx += 1
    if aIdx >= len(aset):
        break
if count == M:
    print(result)
else:
    print(-1)

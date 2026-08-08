from heapq import heappush, heappop

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
# print(A)
# print(B)
aIdx = 0
bIdx = 0
data = []
a = A[aIdx]
b = B[bIdx]
result = 0
heappush(data, (-(a * b), aIdx, bIdx))
idxMemo = set()
# print(data)
for k in range(K):
    num, aIdx, bIdx = heappop(data)
    result -= num
    nextAIdx = aIdx + 1
    nextBIdx = bIdx
    if nextAIdx < N:
        nextNum = A[nextAIdx] * B[nextBIdx]
        idxData = (nextAIdx, nextBIdx)
        if idxData not in idxMemo:
            heappush(data, (-nextNum, nextAIdx, nextBIdx))
            idxMemo.add(idxData)
    nextAIdx = aIdx
    nextBIdx = bIdx + 1
    if nextBIdx < M:
        nextNum = A[nextAIdx] * B[nextBIdx]
        idxData = (nextAIdx, nextBIdx)
        if idxData not in idxMemo:
            heappush(data, (-nextNum, nextAIdx, nextBIdx))
            idxMemo.add(idxData)
    # print(-num, aIdx, bIdx)
print(result)

from sortedcontainers import SortedList
N, D = map(int, input().split())
A = list(map(int, input().split()))
numData = SortedList()
nowIdx = 0
result = 0
for idx in range(N):
    a = A[idx]
    while len(numData) > 0:
        i = numData.bisect_left(a)
        isOk = True
        if i > 0 and a - numData[i - 1] < D:
            isOk = False
        elif i < len(numData) and numData[i] - a < D:
            isOk = False
        if isOk:
            break
        numData.remove(A[nowIdx])
        nowIdx += 1
    numData.add(a)
    result += len(numData)
print(result)

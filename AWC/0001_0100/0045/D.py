from typing import Tuple
from sortedcontainers import SortedSet

def calcNums(N: int)->Tuple[list[int], list[int]]:
    minResult = [0] * (N + 3)
    maxResult = [0] * (N + 3)
    minResult[1] = 1
    maxResult[1] = 1
    for i in range(2, N + 3):
        if minResult[i] > 1:
            continue
        minResult[i] = i
        maxResult[i] = i
        for j in range(i, N + 3, i):
            if minResult[j] == 0:
                minResult[j] = i
            maxResult[j] = i
    return minResult, maxResult

N = int(input())
A = list(map(int, input().split()))
minPList, maxPList = calcNums(max(A))
A.sort()

minNums = SortedSet()
maxNums = SortedSet()
minDataNums = dict()
maxDataNums = dict()
for a in A:
    minDataNums[a] = minDataNums.get(a, 0) + 1
    maxDataNums[a] = maxDataNums.get(a, 0) + 1
    minNums.add(a)
    maxNums.add(a)
minNums.discard(1)
maxNums.discard(1)
# print(minPList, maxPList)
minResult = 0
while minNums:
    x = minNums.pop()
    # 個数
    num = minDataNums[x]
    minDataNums[x] = 0
    p = minPList[x]
    xp = x//p
    minNums.add(xp)
    minResult += num
    minDataNums[xp] = minDataNums.get(xp, 0) + p * num
    minNums.discard(1)
    # print(x, p, minNums, minDataNums)
maxResult = 0
while maxNums:
    x = maxNums.pop()
    # 個数
    num = maxDataNums[x]
    maxDataNums[x] = 0
    p = maxPList[x]
    xp = x//p
    maxNums.add(xp)
    maxResult += num
    maxDataNums[xp] = maxDataNums.get(xp, 0) + p * num
    maxNums.discard(1)
    # print(x, p, maxNums, maxDataNums)
print(minResult, maxResult)


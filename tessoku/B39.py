from collections import defaultdict

from heapq import heappop, heappush
N, D = map(int, input().split())
inputData = defaultdict(list)
for n in range(N):
    x, y = map(int, input().split())
    inputData[x].append(-y)
yData = []
result = 0
for d in range(1, D + 1):
    yList = inputData[d]
    for y in yList:
        heappush(yData, y)
    if len(yData) == 0:
        continue
    result -= heappop(yData)
print(result)

from sortedcontainers import SortedSet
N = int(input())
XYData = []
XY = SortedSet()
ignoreXY = SortedSet()
xMin, xMax = 10 ** 10, -10 ** 10
yMin, yMax = 10 ** 10, -10 ** 10
for n in range(N):
    x, y = map(int, input().split())
    XY.add((-x, y, n+1))
    XYData.append((x, y))
    xMin, xMax = min(xMin, x), max(xMax, x)
    yMin, yMax = min(yMin, y), max(yMax, y)
yMid = (yMax+yMin) // 2
resultTmp = []
while XY:
    x, y, n = XY.pop()
    if y >= yMid:
        ignoreXY.add((-x, y, n))
    resultTmp.append(n)
    # print(-x, y, n)
while ignoreXY:
    x, y, n = ignoreXY.pop()
    resultTmp.append(n)
resIdx = resultTmp.index(1)
result = []
for i in range(N):
    result.append(resultTmp[(resIdx + i) % N])

print(*result)

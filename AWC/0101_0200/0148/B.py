from collections import defaultdict

N = int(input())
X = set()
Y = set()
numX = defaultdict(int)
numY = defaultdict(int)
XY = []
for n in range(N):
    x, y = map(int, input().split())
    X.add(x)
    Y.add(y)
    numX[x] += 1
    numY[y] += 1
    XY.append((x, y))

X = sorted(X)
Y = sorted(Y)
result = []
for x, y in XY:
    Cx, Cy = len(numX), len(numY)
    if numX[x] == 1:
        Cx -= 1
    if numY[y] == 1:
        Cy -= 1
    result.append(Cx * Cy - (N - 1))
print(*result, sep="\n")

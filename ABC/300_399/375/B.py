N = int(input())
result = 0
XY = [(0, 0)]
for n in range(N):
    x, y = [int(l) for l in input().split()]
    XY.append((x, y))
XY.append((0, 0))
for i in range(N + 1):
    result += ((XY[i][0] - XY[i+1][0])**2 + (XY[i][1] - XY[i+1][1])**2)**0.5
print(result)

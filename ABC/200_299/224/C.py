N = int(input())
XY = [[int(l) for l in input().split()] for _ in range(N)]
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            x3, y3 = XY[k]
            if abs((x2 - x1) * (y3 - y1) -(x3 - x1) * (y2 - y1)) > 0:
                result += 1
print(result)

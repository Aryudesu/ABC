import math

N = int(input())
XY = []
for n in range(N):
    XY.append([int(l) for l in input().split()])

data = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x_i, y_i = XY[i]
        x_j, y_j = XY[j]
        a, b = x_i - x_j, y_i - y_j
        g = math.gcd(a, b)
        data.add(tuple([a//g, b//g]))
print(len(data))

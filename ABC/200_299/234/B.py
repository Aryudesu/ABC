N = int(input())
Point = []
for _ in range(N):
    Point.append([int(l) for l in input().split()])

result = 0
for p1 in range(N - 1):
    x1, y1 = Point[p1]
    for p2 in range(p1, N):
        x2, y2 = Point[p2]
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if result < dist:
            result = dist
print(result ** 0.5)

def calc(x1, y1, x2, y2):
    point = set()
    point.add((-2, 1))
    point.add((-2, -1))
    point.add((-1, -2))
    point.add((-1, 2))
    point.add((1, 2))
    point.add((1, -2))
    point.add((2, 1))
    point.add((2, -1))
    for p in point:
        x, y = p
        tmp = (x2 - x1 - x, y2 - y1 - y)
        if tmp in point:
            return True
    return False


x1, y1, x2, y2 = [int(l) for l in input().split()]
if x1 > x2:
    x1, y1, x2, y2 = x2, y2, x1, y1
print("Yes" if calc(x1, y1, x2, y2) else "No")

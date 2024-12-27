def calcABC(x0, y0, x1, y1):
    dx = x0 - x1
    dy = y0 - y1
    a = -dy
    b = dx
    c = -dx * y0 + dy * x0
    return a, b, c

def calcVerticalABC(x0, y0, dx, dy):
    a = dx
    b = dy
    c = -dx * x0 - dy * y0
    return a, b, c

def calcDist(x0, y0, x1, y1, x2, y2):
    if y1 == y2:
        if min([x1, x2]) <= x0 and x0 <= max([x1, x2]):
            return abs(y0 - y2)
        return min([(x0 - x1) ** 2 + (y0 - y1) ** 2, (x0 - x2) ** 2 + (y0 - y2) ** 2]) ** 0.5
    if x1 == x2:
        if min([y1, y2]) <= y0 and y0 <= max([y1, y2]):
            return abs(x0 - x2)
        return min([(x0 - x1) ** 2 + (y0 - y1) ** 2, (x0 - x2) ** 2 + (y0 - y2) ** 2]) ** 0.5
    a, b, c = calcABC(x1, y1, x2, y2)
    d, e, f = calcVerticalABC(x0, y0, x1 - x2, y1 - y2)
    print(a, b, c, d, e, f)
    afcd = a*f - c*d
    bdae = b * d - a * e
    if bdae < 0:
        afcd = -afcd
        bdae = -bdae
    print(afcd, bdae, afcd/bdae)
    if min([y1, y2]) * bdae <= afcd and afcd <= max([y1, y2]) * bdae:
        return abs(a * x0 + b * y0 + c)/((a ** 2 + b ** 2)**0.5)
    return min([(x0 - x1) ** 2 + (y0 - y1) ** 2, (x0 - x2) ** 2 + (y0 - y2) ** 2]) ** 0.5

x0, y0 = [int(l) for l in input().split()]
x1, y1 = [int(l) for l in input().split()]
x2, y2 = [int(l) for l in input().split()]
print(calcDist(x0, y0, x1, y1, x2, y2))

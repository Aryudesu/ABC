def calc():
    x1, y1, r1 = [int(l) for l in input().split()]
    x2, y2, r2 = [int(l) for l in input().split()]
    r1, r2 = max(r1, r2) , min(r1, r2)
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d1 = (r1 - r2) ** 2
    if dist < d1:
        return 1
    elif dist == d1:
        return 2
    d2 = (r1 + r2) ** 2
    if dist < d2:
        return 3
    elif dist == d2:
        return 4
    elif dist > d2:
        return 5

print(calc())

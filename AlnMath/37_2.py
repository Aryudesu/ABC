def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def is_intersect(a, b, c, d):
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    ta = cross(bx-ax, by-ay, cx-ax, cy-ay)
    tb = cross(bx-ax, by-ay, dx-ax, dy-ay)
    tc = cross(dx-cx, dy-cy, ax-cx, ay-cy)
    td = cross(dx-cx, dy-cy, bx-cx, by-cy)

    # 同一直線上
    if ta == tb == tc == td == 0:
        return (
            max(min(ax, bx), min(cx, dx))
            <=
            min(max(ax, bx), max(cx, dx))
        ) and (
            max(min(ay, by), min(cy, dy))
            <=
            min(max(ay, by), max(cy, dy))
        )

    return ta * tb <= 0 and tc * td <= 0

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

print("Yes" if is_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)) else "No")

from math import gcd


def lineIdentifer(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    cx = x1 + x2
    cy = y1 + y2
    a = 2 * dx
    b = -2 * dy
    c = dy * cy + dx * cx
    g = gcd(gcd(abs(a), abs(b)), abs(c))
    a //= g
    b //= g
    c //= g
    if a < 0 or (a == 0 and b < 0):
        a *= -1
        b *= -1
        c *= -1
    return (a, b, c)

def calc()->bool:
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
    li1 = lineIdentifer(px, py, qx, qy)
    li2 = lineIdentifer(rx, ry, sx, sy)
    a1, b1 = li1[0], li1[1]
    g1 = gcd(a1, b1)
    a1, b1 = a1//g1, b1//g1

    a2, b2 = li2[0], li2[1]
    g2 = gcd(a2, b2)
    a2, b2 = a2//g2, b2//g2
    # 傾きが異なれば存在する
    if (a1, b1) != (a2, b2):
        return True
    # 傾きが同じ場合は同一直線上であれば存在
    return li1 == li2


T = int(input())
result = []
for _ in range(T):
    result.append("Yes" if calc() else "No")
print(*result, sep="\n")

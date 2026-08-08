def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

# ps = [(x, y), ...]: ソートされた座標list
def convex_hull(ps):
    qs = []
    N = len(ps)
    for p in ps:
        # 一直線上で高々2点にする場合は ">=" にする
        while len(qs) > 1 and cross3(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(N-2, -1, -1):
        p = ps[i]
        while len(qs) > t and cross3(qs[-1], qs[-2], p) > 0:
            qs.pop()
        qs.append(p)
    return qs

N = int(input())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
XY.sort()
data = convex_hull(XY)
result = 0
for i in range(2, len(data)):
    result += cross3(data[0], data[i-1], data[i])
print(result)

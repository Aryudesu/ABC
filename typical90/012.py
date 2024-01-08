from atcoder.dsu import DSU


def xy2int(y, x, H, W):
    y_ = y - 1
    x_ = x - 1
    if y_ >= 0 and y_ < H and x_ >= 0 and x_ < W:
        return y_ * W + x_
    else:
        return None

H, W = [int(l) for l in input().split()]
dsu = DSU(H * W + 1)
data = set()
Q = int(input())
result = []
for _ in range(Q):
    T, *query = [int(l) for l in input().split()]
    if T == 1:
        r, c = query
        rci = xy2int(r, c, H, W)
        data.add(rci)
        rcj = xy2int(r - 1, c, H, W)
        if not rcj is None and rcj in data:
            dsu.merge(rci, rcj)
            data.add(rcj)
        rcj = xy2int(r + 1, c, H, W)
        if not rcj is None and rcj in data:
            dsu.merge(rci, rcj)
            data.add(rcj)
        rcj = xy2int(r, c - 1, H, W)
        if not rcj is None and rcj in data:
            dsu.merge(rci, rcj)
            data.add(rcj)
        rcj = xy2int(r, c + 1, H, W)
        if not rcj is None and rcj in data:
            dsu.merge(rci, rcj)
            data.add(rcj)
    else:
        ra, ca, rb, cb = query
        rci = xy2int(ra, ca, H, W)
        rcj = xy2int(rb, cb, H, W)
        result.append("Yes" if dsu.same(rci, rcj) and rci in data and rcj in data else "No")

for r in result:
    print(r)

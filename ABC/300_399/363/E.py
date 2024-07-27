from atcoder.dsu import DSU


def hw2num(h, w, H, W):
    return W * h + w

def is_ok(h, w, A, sea):
    return A[h][w] > sea

def get_urld(h, w, H, W):
    result = []
    if h + 1 < H:
        result.append((h + 1, w))
    if h - 1 >= 0:
        result.append((h - 1, w))
    if w + 1 < W:
        result.append((h, w + 1))
    if w - 1 >= 0:
        result.append((h, w - 1))
    return result

H, W, Y = [int(l) for l in input().split()]
A = []
num_data = set()
for h in range(H):
    tmp = [int(l) for l in input().split()]
    A.append(tmp)
    for t in tmp:
        num_data.add(t)
num_data = list(num_data)
num_data.sort(reverse=True)
dsu = DSU(H * W)
result = [[False] * W for _ in range(H)]

map_data = []
for h in range(H):
    for w in range(W):
        if A[h][w] > Y:
            result[h][w] = True

for h in range(H):
    for w in range(W):
        urld = get_urld(h, w, H, W)
        for h2, w2 in urld:
            if A[h2][w2] > Y:
                dsu.merge(hw2num(h, w), hw2num(h2, w2))

for y in range(1, Y + 1):
    pass

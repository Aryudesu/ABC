from collections import defaultdict


def yx2int(y, x, H, W):
    return y * W + x

def is_infield(y, x, dy, dx, H, W):
    return y + dy >= 0 and y + dy < H and x + dx >= 0 and x + dx < W

def calc(H, W, S, A, B, C, D):
    inf = 10 ** 18
    data = defaultdict(lambda: inf)
    st = (A, B)
    gl = (C, D)
    result = inf
    data[st] = 0
    nodes = {st}
    while nodes:
        new_node = set()
        for node in nodes:
            for dh in range(-1, 2):
                for dw in range(-1, 2):
                    if dh != 0 and dw != 0:
                        continue
                    if dh == 0 and dw == 0:
                        continue
                    h, w = node
                    if not is_infield(h, w, dh, dw, H, W):
                        continue
                    nh = h + dh
                    nw = w + dw
                    if S[nh][nw] == ".":
                        now = data[node]
                        nd = (nh, nw)
                        if data[nd] > now:
                            data[nd] = now
                            new_node.add(nd)
                            if nd == gl:
                                result = now
                    elif S[h + dh][w + dw] == "#":
                        now = data[node]
                        nd = (nh, nw)
                        if data[nd] > now + 1:
                            data[nd] = now + 1
                            new_node.add(nd)
                        if is_infield(h, w, dh * 2, dw * 2, H, W):
                            if S[h + dh * 2][w + dw * 2] == "#":
                                nd = (h + dh * 2, w + dw * 2)
                                if data[nd] > now + 1:
                                    data[nd] = now + 1
                                    new_node.add(nd)
        nodes = new_node
    return result

H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())
A, B, C, D = [int(l) - 1 for l in input().split()]
print(calc(H, W, S, A, B, C, D))

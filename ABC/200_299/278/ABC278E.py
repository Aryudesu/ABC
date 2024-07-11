H, W, N, h, w = [int(l) for l in input().split()]
color = dict()
A = []
# 表作成
for y in range(H):
    A.append([int(l) for l in input().split()])
# 色一覧
for x in range(W):
    for y in range(H):
        c = A[y][x]
        tmp = color.setdefault(c, 0)
        color[c] = tmp + 1
cmax = len(color)
# 計算
res = []
for J in range(H - h + 1):
    cl = dict()
    res_tmp = []
    rt = 0
    # 初期で塗られている色
    for x in range(w):
        for y in range(h):
            c = A[J + y][x]
            tmp = cl.setdefault(c, color[c])
            cl[c] = tmp - 1
            if cl[c] == 0:
                rt += 1
    res_tmp.append(cmax - rt)
    for I in range(1, W - w + 1):
        # 塗られていない色
        for y in range(h):
            c = A[J + y][I - 1]
            tmp = cl.setdefault(c, color[c])
            cl[c] = tmp + 1
            if cl[c] == 1:
                rt -= 1
            c = A[J + y][I + w - 1]
            tmp = cl.setdefault(c, color[c])
            cl[c] = tmp - 1
            if cl[c] == 0:
                rt += 1
        res_tmp.append(cmax - rt)
    res.append(res_tmp)
for r in res:
    print(*r)

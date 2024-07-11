def calc(grp, snum, tnum):
    lg = len(grp)
    for sn in snum:
        if sn in tnum:
            return True
    node = snum
    alr = [False] * lg
    for sn in snum:
        alr[sn] = True
    while len(node) > 0:
        tmp = []
        for s in node:
            alr[s] = True
            gar = grp[s]
            for g in gar:
                if g in tnum:
                    return True
                if not alr[g]:
                    tmp.append(g)
        node = tmp
    return False


N = int(input())
sx, sy, tx, ty = [int(l) for l in input().split()]
snum = []
tnum = []
xyr = []
grp = []
for n in range(N):
    x, y, r = [int(l) for l in input().split()]
    sdist = (x - sx) ** 2 + (y - sy) ** 2
    if sdist == r**2:
        snum.append(n)
    tdist = (x - tx) ** 2 + (y - ty) ** 2
    if tdist == r**2:
        tnum.append(n)
    xyr.append([x, y, r])
    xyrlen = len(xyr)
    grp.append([])
    for idx in range(xyrlen - 1):
        # 円が交わる場合
        dist = (xyr[idx][0] - x) ** 2 + (xyr[idx][1] - y) ** 2
        if dist <= (r + xyr[idx][2]) ** 2 and dist >= (r - xyr[idx][2]) ** 2:
            # 該当のグラフ番号に追加
            grp[idx].append(n)
            grp[n].append(idx)


if calc(grp, snum, tnum):
    print("Yes")
else:
    print("No")

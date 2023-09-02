def is_unit_color(data, C, rcd, delnum):
    tmp = rcd.pop()
    rcd.add(tmp)
    c = C[tmp]
    num = data.get(c)
    dn = delnum.get(c, 0)
    if num == len(rcd) + dn:
        delnum[c] = dn + 1
        return c
    return None


H, W = [int(l) for l in input().split()]
HColorNum = [{} for _ in range(H)]
HColorDelNum = [{} for _ in range(H)]
WColorNum = [{} for _ in range(W)]
WColorDelNum = [{} for _ in range(W)]
C = []
CT = [[] for _ in range(W)]

HData = {h for h in range(H)}
WData = {w for w in range(W)}

for h in range(H):
    ipt = input()
    C.append(list(ipt))
    for w in range(W):
        tmp = CT[w]
        tmp.append(ipt[w])

for h in range(H):
    for w in range(W):
        c = C[h][w]
        HColorNum[h][c] = 1 + HColorNum[h].get(c, 0)
        WColorNum[w][c] = 1 + WColorNum[w].get(c, 0)

delflag = True
while delflag:
    delflag = False
    hdeldata = set()
    wdeldata = set()
    if len(WData) > 1:
        for h in HData:
            if is_unit_color(HColorNum[h], C[h], WData, HColorDelNum[h]):
                hdeldata.add(h)
                delflag = True
    if len(HData) > 1:
        for w in WData:
            if is_unit_color(WColorNum[w], CT[w], HData, WColorDelNum[w]):
                wdeldata.add(w)
                delflag = True
    HData -= hdeldata
    WData -= wdeldata
print(len(HData) * len(WData))

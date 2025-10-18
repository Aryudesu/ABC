def debug(H, W, fieldData: set):
    for h in range(H):
        tmp = ""
        for w in range(W):
            if (h, w) in fieldData:
                tmp += "#"
            else:
                tmp += "."
        print(tmp)


H, W = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())

# 最新の黒で塗られたところ
data = set()
# 塗られたところ
fieldData = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            data.add((h, w))
            fieldData.add((h, w))

dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while data:
    newData = set()
    for h, w in data:
        for dh, dw in dist:
            if not (0 <= h + dh < H and 0 <= w + dw < W):
                continue
            nh = h + dh
            nw = w + dw
            tmp = 0
            for ddh, ddw in dist:
                if not (0 <= nh + ddh < H and 0 <= nw + ddw < W):
                    continue
                if (nh + ddh, nw + ddw) in fieldData:
                    tmp += 1
                if tmp >= 2:
                    break
            if tmp == 1 and not (nh, nw) in fieldData:
                newData.add((nh, nw))
    for nd in newData:
        fieldData.add(nd)
    data = newData
# debug(H, W, fieldData)
print(len(fieldData))

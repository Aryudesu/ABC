def cut(A, H, W):
    minW = 10
    maxW = 0
    minH = 10
    maxH = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == "#":
                if minW > w:
                    minW = w
                if minH > h:
                    minH = h
                if maxW < w:
                    maxW = w
                if maxH < h:
                    maxH = h
    result = []
    for h in range(H):
        tmp = []
        for w in range(W):
            if minH <= h and h <= maxH and minW <= w and w <= maxW:
                tmp.append(A[h][w])
        if tmp:
            result.append(tmp)
    return result, maxH - minH + 1, maxW - minW + 1


def judge(A, HA, WA, B, HB, WB, X, HX, WX):
    for ha in range(HX - HA + 1):
        for hb in range(HX - HB + 1):
            for wa in range(WX - WA + 1):
                for wb in range(WX - WB + 1):
                    result = True
                    for h in range(HX):
                        for w in range(WX):
                            # print(ha, hb, wa, wb, h, w)
                            tmp = "."
                            if h >= ha and w >= wa and ha + HA - 1 >= h and wa + WA - 1 >= w:
                                tmp = A[h - ha][w - wa]
                            if tmp != "#" and h >= hb and w >= wb and hb + HB - 1 >= h and wb + WB - 1 >= w:
                                tmp = B[h - hb][w - wb]
                            if tmp != X[h][w]:
                                result = False
                                break
                        if not result:
                            break
                    if result:
                        return True
    return False


HA, WA = [int(l) for l in input().split()]
A = [input() for _ in range(HA)]
HB, WB = [int(l) for l in input().split()]
B = [input() for _ in range(HB)]
HX, WX = [int(l) for l in input().split()]
X = [input() for _ in range(HX)]
AA, HHA, WWA = cut(A, HA, WA)
BB, HHB, WWB = cut(B, HB, WB)
XX, HHX, WWX = cut(X, HX, WX)
# print(AA, BB, XX)
print("Yes" if judge(AA, HHA, WWA, BB, HHB, WWB, XX, HHX, WWX) else "No")

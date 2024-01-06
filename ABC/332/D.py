def isOk(H, W, A, B):
    AData = dict()
    for h in range(H):
        ADatw = []
        for w in range(W):
            ADatw.append(A[h][w])
        ADatw.sort()
        At = tuple(ADatw)
        AData[At] = AData.get(At, 0) + 1
    for h in range(H):
        BDatw = []
        for w in range(W):
            BDatw.append(B[h][w])
        BDatw.sort()
        Bt = tuple(BDatw)
        if AData.get(Bt, 0) == 0:
            return False
        AData[Bt] = AData.get(Bt, 0) - 1
    AData = dict()
    for w in range(W):
        ADatw = []
        for h in range(H):
            ADatw.append(A[h][w])
        ADatw.sort()
        At = tuple(ADatw)
        AData[At] = AData.get(At, 0) + 1
    for w in range(W):
        BDatw = []
        for h in range(H):
            BDatw.append(B[h][w])
        BDatw.sort()
        Bt = tuple(BDatw)
        if AData.get(Bt, 0) == 0:
            return False
        AData[Bt] = AData.get(Bt, 0) - 1
    return True


def calcTe(H, W, A, B):
    AH = []
    BH = []
    result = 0
    for h in range(H):
        atmp = []
        btmp = []
        for w in range(W):
            atmp.append(A[h][w])
            btmp.append(B[h][w])
        AH.append(atmp)
        BH.append(btmp)
    for h1 in range(H - 1):
        ad = [i for i in AH[h1]]
        ad.sort()
        for h2 in range(h1, H):
            bd = [i for i in BH[h2]]
            bd.sort()
            if ad == bd:
                result += abs(h2- h1)
                i = h2
                while i > h1:
                    BH[i] = BH[i-1]
                    i -= 1
                BH[h1] = [i for i in AH[h1]]
                break
    for h1 in range(W - 1):
        ad = [i for i in AH[h1]]
        for h2 in range(h1, W):
            bd = [i for i in BH[h2]]
            if ad == bd:
                result += abs(h2 - h1)
                i = h2
                while i > h1:
                    BH[i] = BH[i-1]
                    i -= 1
                BH[h1] = bd
                break
    return result


def calc(H, W, A, B):
    if not isOk(H, W, A, B):
        return -1
    return calcTe(H, W, A, B)


H, W = [int(l) for l in input().split()]
A = []
B = []
for h in range(H):
    A.append([int(l) for l in input().split()])
for h in range(H):
    B.append([int(l) for l in input().split()])
res  = calc(H, W, A, B)
print(res)
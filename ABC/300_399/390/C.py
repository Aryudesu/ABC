def calc(H, W, LU, RD, S):
    for h in range(LU[0], RD[0] + 1):
        for w in range(LU[1], RD[1] + 1):
            if S[h][w] == ".":
                return False
    return True


H, W = [int(l) for l in input().split()]
LU = [H + 1, W + 1]
RD = [-1, -1]
S = []
for h in range(H):
    tmp = input()
    for w in range(W):
        if tmp[w] == "#":
            tluh, tluw = LU
            trdh, trdw = RD
            LU = [min([tluh, h]), min([tluw, w])]
            RD = [max([trdh, h]), max([trdw, w])]
    S.append(tmp)
# print(LU, RD)
print("Yes" if calc(H, W, LU, RD, S) else "No")

H, W, M = [int(l) for l in input().split()]
memoH = dict()
memoW = dict()
memoC = dict()
BOM = []
for m in range(M):
    h, w = [int(l) for l in input().split()]
    memoH[h] = memoH.get(h, 0) + 1
    memoW[w] = memoW.get(w, 0) + 1
    if h == w:
        memoC[h] = memoC.get(h, 0) + 1
print(memoH, memoW, memoC)

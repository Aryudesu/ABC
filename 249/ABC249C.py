def CalcRList(SL):
    CList = "abcdefghijklmnopqrstuvwxyz"
    RList = [0 for l in CList]
    for S in SL:
        # 入力文字列
        for s in S:
            cind = CList.index(s)
            RList[cind] += 1
    count = 0
    for r in RList:
        if r == K:
            count += 1
    return count


N, K = [int(l) for l in input().split()]
SList = []
Max = 0
BMax = 0
for n in range(N):
    S = input()
    SList.append(S)

Max = 0
for n in range(2**N):
    SL = []
    for m in range(15):
        k = (n >> m) & 1
        if k:
            SL.append(SList[m])
        m = CalcRList(SL)
        if Max < m:
            Max = m
print(Max)

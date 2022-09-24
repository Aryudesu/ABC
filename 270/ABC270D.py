def searchNextIdx(NAI, TN, A, K):
    # 次の山を探索する
    for k in range(NAI + 1, K):
        if A[k] <= TN:
            return k
    return -1


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
# 一旦ソート
A.sort(reverse=True)
# tmpN
TN = N
# now A index
NAI = 0
TAKAHASHI = 0
AOKI = 0
# True:高橋　False:青木
Turn = True
# 一旦無限に続ける
while TN:
    # もしいま見ているAのほうが山の個数より多ければ
    if A[NAI] > TN:
        # 次の山を探索する
        NAI = searchNextIdx(NAI, TN, A, K)
        # 適切なものが見つからなかった場合はループを抜ける
        if NAI == -1:
            break
    # 注目している山
    tmpA = A[NAI]
    # 何回その山から取れるか
    di = TN // tmpA
    # 取った結果何個余るか
    dm = TN % tmpA
    # 高橋と青木の取った個数
    TAKAHASHI += (di // 2) * tmpA
    AOKI += (di // 2) * tmpA
    # 奇数回なら先に取った人が1回分多い
    if di % 2:
        if Turn:
            TAKAHASHI += tmpA
        else:
            AOKI += tmpA
        Turn = not Turn
    # 余った個数のが次の山の個数
    TN = dm
print(TAKAHASHI)
print(AOKI)

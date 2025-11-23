from sortedcontainers import SortedList

def getWDL(a: str, b: str, gcpData: dict) -> int:
    """aとbの試合結果の取得"""
    an = gcpData[a]
    bn = gcpData[b]
    if an == bn:
        return 0
    if (an + 1) % 3 == bn:
        return 1
    if (an + 2) % 3 == bn:
        return -1
    raise Exception()

N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
GCPdata = {"G":0, "C": 1, "P": 2}
data = SortedList()
# スコア昇順なので成績良い程スコアはマイナスにする
for n in range(2*N):
    data.add((0, n))
# M回試合をする
for m in range(M):
    nextData = SortedList()
    for k in range(N):
        aidx = 2*k
        bidx = 2*k + 1
        AScore, ANum = data[aidx]
        BScore, BNum = data[bidx]
        wdl = getWDL(A[ANum][m], A[BNum][m], GCPdata)
        if wdl== 1:
            AScore -= 1
        elif wdl == -1:
            BScore -= 1
        nextData.add((AScore, ANum))
        nextData.add((BScore, BNum))
    data = nextData
#     print(data)
# print(data)
for sc, num in data:
    print(num + 1)

def calc(N, XY, S):
    for n in range(N):
        x = XY[n][0]
        y = XY[n][1]
        if S[n] == "L":
            # 取得
            l = dataL.get(y)
            # y座標のデータが存在する場合
            if l is not None:
                # もしもっと右に人が存在する場合
                if x > l:
                    dataL[y] = x
            else:
                dataL[y] = x
        else:
            # 取得
            l = dataR.get(y)
            # y座標のデータが存在する場合
            if l is not None:
                # もしもっと左に人が存在する場合
                if x < l:
                    dataR[y] = x
            else:
                dataR[y] = x
    for k in dataL:
        r = dataR.get(k)
        if r is not None:
            if dataL[k] > r:
                return "Yes"
    return "No"


N = int(input())
XY = []
for n in range(N):
    XY.append([int(l) for l in input().split()])
S = input()
dataR = dict()
dataL = dict()
print(calc(N, XY, S))

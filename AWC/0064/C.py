N, M = map(int, input().split())
data = dict()
# data[経過時間] = 評価点
data[0] = 0
for n in range(N):
    newData = data.copy()
    r, t = map(int, input().split())
    for nowT, nowV in data.items():
        newT = t + nowT
        newV = r + nowV
        if newT > M:
            continue
        if newT not in newData or newData[newT] < newV:
            newData[newT] = newV
    data = newData
print(max(newData.values()))

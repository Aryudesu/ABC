N, M = map(int, input().split())
# data[値段] = 最大価値
data = [{0:0}]
maxVal = 0
maxKey = set()
PV = []
for n in range(N):
    nextData = data[-1].copy()
    p, v = map(int, input().split())
    PV.append((p, v))
    for k, c in data[-1].items():
        nextNum = p + k
        nextVal = c + v
        if p + k > M:
            continue
        nextData[nextNum] = max(nextData.get(nextNum, 0), nextVal)
        if nextVal > maxVal:
            maxVal = nextVal
            maxKey = set()
            maxKey.add(nextNum)
        elif nextVal == maxVal:
            maxKey.add(nextNum)
    data.append(nextData)
result = [0] * N
for idx in range(N, 0, -1):
    pat = 0
    p, v = PV[idx - 1]
    nextMaxKey = set()
    # 最高価値の値段についてのループ
    for key in maxKey:
        val = data[idx].get(key)
        if (key - p) in data[idx - 1]:
            if data[idx - 1][key - p] == val - v:
                result[idx - 1] |= 2
                nextMaxKey.add(key - p)
        if key in data[idx - 1]:
            if data[idx-1][key] == val:
                result[idx - 1] |= 1
                nextMaxKey.add(key)
    maxKey = nextMaxKey
for r in result:
    if r <= 1:
        print("C", end="")
    elif r == 2:
        print("A", end="")
    elif r == 3:
        print("B", end="")
print()

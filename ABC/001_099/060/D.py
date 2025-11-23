N, W = map(int, input().split())
data = {0: 0}
result = 0
for n in range(N):
    w1, v1 = map(int, input().split())
    newData = data.copy()
    for w2 in data:
        v2 = data.get(w2, 0)
        if w1 + w2 > W:
            continue
        newData[w2 + w1] = max(data.get(w2, 0) + v1, newData.get(w2 + w1, 0))
        result = max(result, newData[w2 + w1])
    data = newData
print(result)

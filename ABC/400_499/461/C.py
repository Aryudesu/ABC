from collections import defaultdict
N, K, M = map(int, input().split())
data = defaultdict(int)
valueData = []
for n in range(N):
    c, v = map(int, input().split())
    if c in data and v < data[c]:
        valueData.append(v)
    else:
        if c in data:
            valueData.append(data[c])
        data[c] = v
maxVals = []
for key in data:
    maxVals.append(data[key])
maxVals.sort()
# print(valueData)
# print(maxVals)
result = 0
for m in range(M):
    val = maxVals.pop()
    result += val
while maxVals:
    valueData.append(maxVals.pop())
valueData.sort()
for n in range(K-M):
    result += valueData.pop()
print(result)

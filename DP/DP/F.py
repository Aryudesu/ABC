from collections import defaultdict

INF = 10**18
S = input()
T = input()
tCharIdx = defaultdict(list)
for idx in range(len(T)):
    tCharIdx[T[idx]].append(idx)

data = [[0]*len(T) for _ in range(len(S))]
idxData = [[(-1, -1)] * len(T) for _ in range(len(S))]
for tIdx in tCharIdx[S[0]]:
    data[0][tIdx] = 1
for sIdx in range(1, len(S)):
    s = S[sIdx]
    tMax = 0
    tMaxIdx = -1
    for tIdx in range(len(T)):
        t = T[tIdx]
        if s == t:
            data[sIdx][tIdx] = tMax + 1
            idxData[sIdx][tIdx] = (sIdx-1, tMaxIdx)
        else:
            data[sIdx][tIdx] = data[sIdx-1][tIdx]
            idxData[sIdx][tIdx] = idxData[sIdx-1][tIdx]
        if tMax < data[sIdx-1][tIdx]:
            tMax = data[sIdx-1][tIdx]
            tMaxIdx = tIdx

# for dat in idxData:
#     print(dat)
    
resTIdx = -1
nowMax = 0
for tIdx in range(len(T)):
    if nowMax < data[-1][tIdx]:
        resTIdx = tIdx
        nowMax = data[-1][tIdx]
result = []
resSIdx = len(S)-1
while resTIdx >= 0:
    result.append(T[resTIdx])
    resSIdx, resTIdx = idxData[resSIdx][resTIdx]
result.reverse()
print("".join(result))

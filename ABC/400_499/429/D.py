from bisect import bisect_left, bisect_right

from collections import defaultdict

N, M, C = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
# スタートからそこにいる場所までに何人の人がいるか数える
data = defaultdict(int)
ss = set()
for a in A:
    data[a] += 1
    ss.add(a)
ssList = list(ss)
ssList.sort()
# i + 0.5秒後に出会った人の数と距離
listNumData = [0]
listDstData = [0]
s = 0
for d in ssList:
    if d == 0:
        continue
    s += data[d]
    listNumData.append(s)
    listDstData.append(d)
for d in ssList:
    s += data[d]
    listNumData.append(s)
    listDstData.append(M + d)
# print(listNumData)
# print(listDstData)

L = len(listNumData)
result = 0
for i in range(L):
    if listDstData[i] >= M:
        break
    base = listNumData[i]
    idx = bisect_left(listNumData, base + C)
    # print(i, idx)
    result += (listNumData[idx] - base) * (min(listDstData[i + 1], M) - listDstData[i])
print(result)

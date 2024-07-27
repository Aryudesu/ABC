N = int(input())
# 各桁個数一覧表
data = [9, 9]
for idx in range(2, 36):
    data.append(data[idx - 2] * 10)
data[0] += 1
# その桁全部までの個数
Sdata = []
s = 0
for dat in data:
    s += dat
    Sdata.append(s)
keta = 0
for idx in range(len(Sdata)):
    if N < Sdata[idx] + 1:
        keta = idx + 1
        break
result = []
if keta > 2:
    Ntmp = N - Sdata[keta - 2]
    Ndata = list(str(Ntmp))
    for nd in range(len(Ndata)):
        Ndata[nd] = int(Ndata[nd])
    print(Ndata)
elif keta == 2:
    print(f"{N % 10 + 1}{N % 10 + 1}")
elif keta == 1:
    print(N - 1)

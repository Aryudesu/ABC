N = int(input())
C = [0] * N
data = []
for i in range(N):
    tmp = input()
    dat = set()
    for j in range(N):
        if tmp[j] == "#":
            dat.add(j)
    data.append(dat)
    C[i] = (len(dat), i)
C.sort()
deskData = set()
okCount = 0
# 候補が少ないものを優先的に入れる
for n, idx in C:
    dat = data[idx]
    f = False
    for d in dat:
        if d in deskData:
            continue
        f = True
        deskData.add(d)
        okCount += 1
        break
print(okCount)

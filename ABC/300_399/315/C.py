N = int(input())
FS = dict()
Fset = set()
for n in range(N):
    F, S = [int(l) for l in input().split()]
    tmp = FS.get(F, [])
    if len(tmp) == 0:
        tmp.append(S)
    elif len(tmp) == 1:
        if tmp[0] >= S:
            tmp.append(S)
        else:
            tmp.append(tmp[0])
            tmp[0] = S
    elif len(tmp) == 2:
        if tmp[0] < S:
            tmp[1] = tmp[0]
            tmp[0] = S
        elif tmp[1] < S:
            tmp[1] = S
    FS[F] = tmp
Datas = []
Somes = []
for key in FS:
    tmp = FS.get(key, [0])
    Datas.append(tmp[0])
    if len(tmp) == 2:
        Somes.append(tmp[0] + tmp[1]//2)
Datas.sort()
maxs = 0
if len(Datas) >= 2:
    maxs = Datas[-1] + Datas[-2]
Somes.sort()
if Somes:
    if maxs < Somes[-1]:
        maxs = Somes[-1]
print(maxs)

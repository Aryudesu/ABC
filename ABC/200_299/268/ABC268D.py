def t2num(S, T):
    tDat = T.split("_")
    count = 0
    result = 0
    for i in range(len(tDat)):
        td = tDat[i]
        tmp = S.get(td)
        if tmp:
            result = tmp
    return result


N, M = [int(l) for l in input().split()]
S = dict()
T = []

for n in range(N):
    S[n] = input()

for m in range(M):
    T.append(input())

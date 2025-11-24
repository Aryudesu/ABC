def enc(data: str, encBase: dict[str, str])-> str:
    result = ""
    for d in data:
        result += encBase[d]
    return result

alp = "abcdefghijklmnopqrstuvwxyz"
X = input()
encBase = dict()
# 元のアルファベットの並び順に対応させて書き換える
for i in range(len(alp)):
    encBase[X[i]] = alp[i]
N = int(input())
Slist = []
encData = dict()
for n in range(N):
    S = input()
    eS = enc(S, encBase)
    encData[eS] = S
    Slist.append(eS)
Slist.sort()
for res in Slist:
    print(encData[res])

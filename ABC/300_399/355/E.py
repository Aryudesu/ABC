def calcIJ(L, R, data):
    i, j = 0, 0
    for dat in data:
        if L % dat[0] == 0:
            tmp = L // dat[0]
            if dat[0] * (tmp + 1) - 1 > R:
                break
            if tmp >= 1:
                i = dat[1]
                j = tmp
        else:
            break
    return (i, j)

def getMinR(R, data):
    for dat in data:
        if R <= dat:
            return dat
    return R

N, L, R = [int(l) for l in input().split()]
data = [(2 ** n, n) for n in range(19)]
ijDat = []
result = 0
l = L
r = R
tmp = []
while l <= R:
    # 質問考えフェーズ
    # iの値を考える
    i, j = calcIJ(l, r, data)
    tmp.append((i,j))
    l = (2 ** i) * (j + 1)
ijDat = tmp

l = 0
r = R
tmp1 = []
while l <= R:
    # 質問考えフェーズ
    # iの値を考える
    i, j = calcIJ(l, r, data)
    tmp.append((i,j))
    l = (2 ** i) * (j + 1)
l = L - 1
r = R
tmp2 = []
while l <= R:
    # 質問考えフェーズ
    # iの値を考える
    i, j = calcIJ(l, r, data)
    tmp.append((i,j))
    l = (2 ** i) * (j + 1)
if len(ijDat) > len(tmp1) + len(tmp2):
    ijDat = tmp1 + tmp2

for i, j in ijDat:
    print("?", i, j)
    T = int(input())
    if T == -1:
        break
    else:
        result = (result + T) % 100
    if l == R:
        break
print("!", result)

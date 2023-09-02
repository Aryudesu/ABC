def calc(d, X):
    res = 0
    for x in X:
        res = res * d + int(x)
    return res


X = input()
M = int(input())
l = len(X)

d = int(max(X))
NMax = 10**100
NMin = 0
res = 0
if l > 1:
    while NMax - NMin > 1:
        med = (NMax + NMin)//2
        if calc(med,X) > M:
            NMax = med
        else:
            NMin = med
    if NMin - d > 0:
        print(NMin - d)
    else:
        print(0)
else:
    if int(X) > M:
        print(0)
    else:
        print(1)

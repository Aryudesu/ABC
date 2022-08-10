S = input()
T = input()
SL = len(S)
TL = len(T)
res = 10000
for idx in range(SL-TL+1):
    tmp = 0
    for idx2 in range(TL):
        if T[idx2] != S[idx + idx2]:
            tmp+=1
    if res > tmp:
        res = tmp
print(res)

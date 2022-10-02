N = int(input())
NN = N // 16
NM = N % 16
res = ''
s = 'ABCDEF'
if NN >= 10:
    res += s[NN - 10]
else:
    res += str(NN)
if NM >= 10:
    res += s[NM - 10]
else:
    res += str(NM)
print(res)

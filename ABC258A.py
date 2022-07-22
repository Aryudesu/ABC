K = int(input())
H = 21 + K//60
M = K%60
res = ''
res += str(H)
res += ':'
if M >= 10:
    res += str(M)
else:
    res += '0' + str(M)
print(res)

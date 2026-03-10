MOD = 10007
K, M = map(int, input().split())
subMod = 9 * MOD * M
CL = []
for k in range(K):
    c, l = map(int, input().split())
    CL.append((c, l))
result, lSum = 0, 0
for i in range(K):
    c, l = CL[-1-i]
    result = (result + c * (pow(10, l, subMod) - 1) * pow(10, lSum, subMod)) % subMod
    lSum += l
print(result//9//M)

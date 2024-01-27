def calcBit(N):
    result = []
    tmpN = N
    while tmpN:
        result.append(tmpN % 2)
        tmpN //= 2
    result.reverse()
    return result


N = int(input())
M = 0
tmp = 1
# 人数計算
while N > tmp:
    tmp *= 2
    M += 1
print(M)
data = dict()
# 飲むやつ計算
for i in range(1, N + 1):
    b = calcBit(i)
    for m in range(1, M + 1):
        if len(b) <= m - 1:
            break
        if b[-m] == 1:
            tmp = data.get(m, [])
            tmp.append(i)
            data[m] = tmp
for i in range(1, M + 1):
    tmp = data.get(i, [])
    print(len(tmp), *tmp)

S = input()
result = 0
tmp = 1
for i in range(M):
    if S[i] == "1":
        result += tmp
    tmp *= 2
print(result if result else N)

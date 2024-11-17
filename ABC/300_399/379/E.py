N = int(input())
S = input()
data = [0]
kuri = []
tmp = 0
for i in range(N):
    tmp += int(S[i]) * (i + 1)
    # その桁（暫定）
    data.append(tmp % 10)
    # 繰り上がり
    kuri.append(tmp//10)
# 1の位は繰り上がりされない
kuri.append(0)
for i in range(N - 1, 0, -1):
    # 次の桁に繰り上げするものはする
    kuri[i - 1] += (kuri[i] + data[i]) // 10
    # 繰り上がってきたのを足す
    data[i] = (data[i] + kuri[i]) % 10
data[0] += kuri[0]
st = 0 if data[0] > 0 else 1
for i in range(st, len(data)):
    print(data[i], end = "")
print()

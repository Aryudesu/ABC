N = int(input())
T = input()
# 先頭
oneCount  = 1 if T[0] == "1" else 0
zeroCount = 1 if T[0] == "0" else 0
for idx in range(1, N):
    nowT = T[idx]
    # 今の文字
    if nowT == "0":
        oneCount, zeroCount = oneCount + zeroCount, zeroCount + oneCount
    else:
        oneCount, zeroCount = oneCount + 1, zeroCount
print(oneCount)

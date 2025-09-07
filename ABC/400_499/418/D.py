N = int(input())
T = input()
# 先頭
zeroZeroCount = 0
zeroOneCount = 0
zeroCount = 0
result = 0
for t in T:
    if t == "0":
        zeroCount = (zeroCount + 1) % 2
    else:
        result += 1
    if zeroCount == 0:
        result += zeroZeroCount
        zeroZeroCount += 1
    else:
        result += zeroOneCount
        zeroOneCount += 1
print(result)

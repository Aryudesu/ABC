N = int(input())
# Nの倍がM
M = 2 * N
print(M)
#
NumLen = N // 4
res = ""
for i in range(NumLen):
    res += "4"
if N % 4:
    res = str(N % 4) + res
print(res)

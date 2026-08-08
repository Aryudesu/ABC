N, M = map(int, input().split())
XC = []
for n in range(N):
    x, c = map(int, input().split())
    XC.append((x, c))
result = 0
s = 0
l = 0
for r in range(N):
    s += XC[r][1]
    while l < r and s > M:
        s -= XC[l][1]
        l += 1
    # print("debug", l, r, s)
    tmp = XC[r][0] - XC[l][0]
    result = max(result, tmp)
print(result)

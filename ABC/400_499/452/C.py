N = int(input())
AB = []
for n in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
# [文字列長さ][存在文字]
Sdata = [[set() for _ in range(11)] for _ in range(11)]
M = int(input())
S = []
for m in range(M):
    s = input()
    L = len(s)
    for i in range(L):
        c = s[i]
        Sdata[L][i+1].add(c)
    S.append(s)
# for dat in Sdata:
#     print(dat)
result = []
for s in S:
    L = len(s)
    if N != L:
        result.append("No")
        continue
    isOk = True
    for i in range(L):
        a, b = AB[i]
        c = s[i]
        if c not in Sdata[a][b]:
            isOk = False
            break
    result.append("Yes" if isOk else "No")
for r in result:
    print(r)

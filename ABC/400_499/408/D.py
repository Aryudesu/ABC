T =  int(input())
res = []
for _ in range(T):
    N = int(input())
    S = input().strip()

    l = S.find('1')
    if l == -1:
        res.append("0")
        continue
    r = S.rfind('1')
    res.append(str(S[l:r+1].count('0')))

for r in res:
    print(r)




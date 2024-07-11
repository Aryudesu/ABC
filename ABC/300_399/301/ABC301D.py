S = list(input())
S.reverse()
N = int(input())
num = 0
data = []
t = 1
for idx in range(len(S)):
    s = S[idx]
    tmp = 1 << idx
    if s == "?":
        data.append(tmp)
    elif s == "1":
        num |= tmp
data.sort(reverse=True)
if num > N:
    print(-1)
else:
    result = num
    for dat in data:
        if (result | dat) <= N:
            result |= dat
    print(result)

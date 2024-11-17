N, K = [int(l) for l in input().split()]
S = input()
data = []
c = 0
for s in S:
    if s == "O":
        c += 1
    else:
        if c > 0:
            data.append(c)
        c = 0
if c > 0:
    data.append(c)
result = 0
for dat in data:
    tmp = dat
    while tmp >= K:
        tmp -= K
        result += 1
print(result)

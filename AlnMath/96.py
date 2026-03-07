N = int(input())
T = list(map(int, input().split()))
S = sum(T)
data = {0}
for t in T:
    nextData = data.copy()
    for dat in data:
        if (dat + t) * 2 > S:
            continue
        nextData.add(dat + t)
    data = nextData
print(S-max(data))

N, K = map(int, input().split())
C = list(map(int, input().split()))
data = {0}
for c in C:
    newData = data.copy()
    for dat in data:
        if dat + c <= K:
            newData.add(dat + c)
    data = newData
print(max(newData))

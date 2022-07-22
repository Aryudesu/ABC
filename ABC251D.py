W = int(input())
res = []
for i in range(99):
    res.append(str((i+1)))
    res.append(str((i+1) * 100))
    res.append(str((i+1) * 10000))
print(len(res))
print(' '.join(res))

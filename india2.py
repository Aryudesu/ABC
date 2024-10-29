data = dict()
memo = set()
count = 0
for i in range(1, 10):
    for j in range(1, 10):
        k = (i * j) % 10
        tmp = data.get(k, list())
        dat1 = (i, j)
        dat2 = (j, i)
        if dat1 in memo or dat2 in memo:
            continue
        datl = [dat1, dat2]
        datl.sort()
        tmp.append(datl[0])
        memo.add(datl[0])
        data[k] = tmp
        count += 1
for i in range(10):
    print(i)
    print(*data.get(i, []))
print(count)

count = 0
data = dict()
memo = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a == c and b + d == 10:
                    continue
                if a == b and c + d == 10:
                    continue
                if c == d and a + b == 10:
                    continue
                k = a * d + b * c
                dat1 = (a, b, c, d)
                dat2 = (d, b, c, a)
                dat3 = (a, c, b, d)
                dat4 = (d, c, b, a)
                dat5 = (b, a, d, c)
                dat6 = (c, a, d, b)
                dat7 = (b, d, a, c)
                dat8 = (c, d, a, b)
                if dat1 in memo or dat2 in memo or dat3 in memo or dat4 in memo or dat5 in memo or dat6 in memo or dat7 in memo or dat8 in memo:
                    continue
                dlist = [dat1, dat2, dat3, dat4, dat5, dat6, dat7, dat8]
                dlist.sort()
                dat = dlist[0]
                if k % 10 == 0:
                    tmp = data.get(k, list())
                    tmp.append(dat)
                    data[k] = tmp
                    memo.add(dat)
                    count += 1
for i in range(1, 14):
    if i*10 in data:
        data[i*10].sort()
        print(i*10)
        print(*data.get(i * 10, []))

print(count)

T = 10
result = dict()
for i in range(1, T + 1):
    for j in range(2, T + 1):
        for k in range(1, j):
            tmp2 = (2**i) % (2**j - 2**k)
            tmp = result.get(tmp2 % 10, set())
            tmp3 = (i, j, k)
            tmp.add(tmp3)
            result[tmp2 % 10] = tmp
keys = []
for k in result:
    keys.append(k)
keys.sort()
for k in keys:
    print(k, result.get(k, []))

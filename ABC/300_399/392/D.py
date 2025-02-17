N = int(input())
K = []
P = []
data = []
for n in range(N):
    k, *p = [int(l) for l in input().split()]
    K.append(k)
    P.append(set(p))
    d = dict()
    for pn in p:
        d[pn] = d.get(pn, 0) + 1
    data.append(d)
# print(data)
result = 0
for n in range(N - 1):
    for m in range(n + 1, N):
        dnum = P[n] & P[m]
        otNum = 0
        for num in dnum:
            otNum += data[n].get(num, 0) * data[m].get(num, 0)

        oneD = K[n]
        twoD = K[m]
        tmp = otNum/(oneD * twoD)
        result = max([result, tmp])
        # print(n, m, otNum, oneD, twoD, tmp)
print(result)

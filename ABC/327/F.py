import bisect

N, D, W = [int(l) for l in input().split()]
xdatadic = dict()
tdatadic = dict()
xdata = []
tdata = []
point = []
for n in range(N):
    t, x = [int(l) for l in input().split()]
    point.append([t, x])
    tmp = xdatadic.get(x, set())
    tmp.add(t)
    xdatadic[x] = tmp
    tmp = tdatadic.get(t, set())
    tmp.add(x)
    tdatadic[t] = tmp
    xdata.append(x)
    tdata.append(t)
xdata.sort()
tdata.sort()
result = []
for i in range(len(xdata)):
    tmp1 = xdata[i]
    count = 0
    for j in range(i, len(xdata)):
        count = xdatadic.get(xdata[j], [])

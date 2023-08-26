N, M = [int(l) for l in input().split()]
TX = []
CO = []
data = dict()
cs = 0
for n in range(N):
    t, x = [int(l) for l in input().split()]
    if t == 2:
        CO.append(x)
    else:
        TX.append([t, x])
CO.sort(reverse=True)
cs = 0
count = 0
data[(0, 0)] = 0
for co in CO:
    cs += co
    count += 1
    data[(count, cs)] = 0
result = 0
for tx in TX:
    t, x = tx
    new_data = dict()
    for key in data:
        val = data.get(key, 0)
        new_data[key] = val
        co, cs = key
        if co >= M:
            continue
        if t == 1 and cs == 0:
            continue
        n_cs = cs
        if t == 1:
            n_cs = cs - 1
        tmp = new_data.get((co + 1, n_cs), 0)
        if tmp < val + x:
            new_data[(co + 1, n_cs)] = val + x
            if result < val + x:
                result = val + x
    # print(data)
    data = new_data
print(result)

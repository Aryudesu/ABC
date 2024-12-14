N, X, K = [int(l) for l in input().split()]
PUC = []
data = [dict()] * (X + 1)
for n in range(N):
    PUC.append([int(l) for l in input().split()])

result = 0
for p, u, c in PUC:
    new_key = tuple([c])
    new_v = u
    new_x = p
    if new_x > X:
        continue
    data[new_x][new_key] = max([new_v, data[new_x].get(new_key, 0)])
    result = max([result, data[new_x][new_key]])
# 0から処理
for x in range(X + 1):
    # x円の時のデータ取得する
    dat = data[x]
    new_dat = dict()
    keys = list(dat.keys())
    # 現時点でのx円のデータについて走査
    for k in keys:
        # 各色の組み合わせについての価値
        v = dat.get(k, 0)
        k_list = list(k)
        k_list.append(None)
        k_set = set(k)
        k_num = len(k_set)
        # 各商品について
        for p, u, c in PUC:
            new_x = x + p
            if new_x > X:
                continue
            new_v = v + u
            new_key = k
            if not c in k_set:
                k_list[-1] = c
                new_key = tuple(k_list)
                new_v += K
            data[new_x][new_key] = max([data[new_x].get(new_key, 0), new_v])
            result = max([result, data[new_x][new_key]])
print(data)
print(result)

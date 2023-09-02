N, K, D, *A = map(int, open(0).read().split())
dic = {(0, 0): 0}
for a in A:
    next_dic = {}
    for k in dic:
        next_dic[k] = max([next_dic.get(k, 0), dic[k]])
        if k[0] < K:
            nkey = (k[0] + 1, (k[1] + a) % D)
            next_dic[nkey] = max([next_dic.get(nkey, 0), dic[k] + a])
    dic = next_dic
print(dic.get((K, 0), -1))

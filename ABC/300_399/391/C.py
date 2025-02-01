N, Q = [int(l) for l in input().split()]
# 鳩[i] = いる場所
data = dict()
for n in range(N):
    data[n] = n
# 場所に何匹いるか
pos = [1] * N
# 何個の巣が複数いるか
res = set()
result = []
for _ in range(Q):
    query = [int(l) - 1 for l in input().split()]
    if query[0] == 0:
        n, P, H = query
        # 場所取得
        p = data[P]
        pos[p] -= 1
        pos[H] += 1
        data[P] = H
        if pos[p] < 2:
            res.discard(p)
        if pos[H] >= 2:
            res.add(H)
    elif query[0] == 1:
        result.append(len(res))
for r in result:
    print(r)

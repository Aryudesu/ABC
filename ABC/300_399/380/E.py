from atcoder.dsu import DSU

N, Q = [int(l) for l in input().split()]
# data[代表] = [色, 最小, 最大]
color = [[n, n, n] for n in range(N)]
    # color[色] = マスの数
num = [1] * N

def update(dsu, x, c):
    # xの代表点取得
    x_l = dsu.leader(x)
    xco, xmi, xma = color[x_l]
    if xco == c:
        return

    x_num = xma - xmi + 1
    num[xco] -= x_num

    newmi, newma = xmi, xma
    if xmi > 0:
        l_l = dsu.leader(xmi - 1)
        lco, lmi, lma = color[l_l]
        if lco == c:
            newmi = lmi
            dsu.merge(x, xmi - 1)
    if xma < N - 1:
        r_l = dsu.leader(xma + 1)
        rco, rmi, rma = color[r_l]
        if rco == c:
            newma = rma
            dsu.merge(x, xma + 1)
    n_l = dsu.leader(x)
    color[n_l] = [c, newmi, newma]
    num[c] += x_num


dsu = DSU(N)
result = []
for _ in range(Q):
    query = [int(l) - 1 for l in input().split()]
    if query[0] == 0:
        q, x, c = query
        update(dsu, x, c)
    elif query[0] == 1:
        q, c = query
        result.append(num[c])
for r in result:
    print(r)

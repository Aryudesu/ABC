def calc(N, S, A):
    data = [0]
    dset = {0}
    sa = 0
    for a in A:
        sa += a
        data.append(sa)
        dset.add(sa)
    # 部分列の残りで作りたい和
    smsa = S % sa
    if smsa == 0:
        return True
    # 間を抜いたらその値は作れる
    num = sa - smsa
    for da in data:
        if da < smsa:
            continue
        if da - smsa in dset:
            return True
    for da in data:
        if da < num:
            continue
        if da - num in dset:
            return True
    return False


N, S = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if calc(N, S, A) else "No")

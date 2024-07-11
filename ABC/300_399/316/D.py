INF = 10000000000000


def calc(zsum, takaz, XYZ):
    # 新規に取り込みたい最低人数
    mokuhyou = zsum//2 + 1 - takaz
    # dp[議席数] = 鞍替え最低人数
    # 0議席は0人
    dp = dict()
    dp[0] = 0
    # 各選挙区でDPしていく
    for xyz in XYZ:
        # 人数，議席数
        num, z = xyz
        # その議席を考える際のデータ
        new_dp = dict()
        new_dp[z] = num
        # 議席数でループ回す
        for d in dp:
            # その議席数の最低人数
            tmp = dp[d]
            # 議席
            tmp2 = new_dp.get(d, INF)
            if tmp2 > tmp:
                new_dp[d] = tmp
            # 次の議席数
            tmp3 = new_dp.get(d + z, INF)
            if tmp3 > tmp + num:
                new_dp[d + z] = tmp + num
        dp = new_dp
    result = INF
    for d in dp:
        if d < mokuhyou:
            continue
        num = dp[d]
        if result > num:
            result = num
    return result


N = int(input())
XYZ = []
zsum = 0
takaz = 0
for n in range(N):
    x, y, z = [int(l) for l in input().split()]
    zsum += z
    if x < y:
        # その区の議席取得に必要な人数, 議席数
        XYZ.append(((y - x)//2 + 1, z))
    else:
        takaz += z
print(calc(zsum, takaz, XYZ))

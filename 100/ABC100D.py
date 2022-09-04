N, M = [int(l) for l in input().split()]
xyz = []
for n in range(N):
    xyz.append([int(l) for l in input().split()])

prev_data = [[xyz[n], xyz[n]] for n in range(N)]
if M > 0:
    for m in range(M - 1):
        next_data = [[[None, None, None], [None, None, None]] for _ in range(N)]
        # 前のケーキ
        for n in range(m, N - M + m + 1):
            # 次のケーキ
            for l in range(n + 1, N - M + m + 2):
                # 次の評価
                xp = prev_data[n][0][0] + xyz[l][0]
                yp = prev_data[n][0][1] + xyz[l][1]
                zp = prev_data[n][0][2] + xyz[l][2]
                xm = prev_data[n][1][0] + xyz[l][0]
                ym = prev_data[n][1][1] + xyz[l][1]
                zm = prev_data[n][1][2] + xyz[l][2]
                # 両方未評価の場合
                if next_data[l][0][0] is None and next_data[l][1][0] is None:
                    next_data[l][0] = [xp, yp, zp]
                    next_data[l][1] = [xm, ym, zm]
                else: 
                    # 大きい方が評価済みの場合
                    if next_data[l][0][0] is not None:
                        if xp + yp + zp < next_data[l][0][0] + next_data[l][0][1] + next_data[l][0][2]:
                            next_data[l][0] = [xp, yp, zp]
                        if next_data[l][1][0] is None:
                            next_data[l][1] = [xm, ym, zm]
                    # 小さい方が評価済みの場合
                    if next_data[l][1][0] is not None:
                        if xm + ym + zm > next_data[l][1][0] + next_data[l][1][1] + next_data[l][1][2]:
                            next_data[l][1] = [xm, ym, zm]
                        if next_data[l][0][0] is None:
                            next_data[l][0] = [xp, yp, zp]
        prev_data = next_data
    res = 0
    for n in range(N):
        if prev_data[n][0][0] is not None:
            tmp = abs(prev_data[n][0][0]) + abs(prev_data[n][0][1]) + abs(prev_data[n][0][2])
            if res < tmp:
                res = tmp
        if prev_data[m][1][0] is not None:
            tmp = abs(prev_data[n][1][0]) + abs(prev_data[n][1][1]) + abs(prev_data[n][1][2])
            if res < tmp:
                res = tmp
else:
    res = 0

print(res)

def calc(N: int, M: int, K: int, ASBT: list[list[int]])->int:
    schedule = []
    for m in range(M):
        a, s, b, t = ASBT[m]
        schedule.append((t + K, 0, m))
        schedule.append((s, 1, m))
    schedule.sort()
    # 各スケジュールの出発時間時点での最良時間をわかりやすくするためのデータ
    depBest = [0] * (M + 1)
    # 着陸直後の最良データ一覧
    aprBest = [0] * (N + 1)

    res = 0
    for tm, num, idx in schedule:
        a, s, b, t = ASBT[idx]
        # 到着
        if num == 0:
            # 着陸後の最良データを書き換える
            aprBest[b] = max(aprBest[b], depBest[idx])
        # 離陸
        elif num == 1:
            # 離陸した際の最良データをメモする
            depBest[idx] = aprBest[a] + 1
            res = max(res, depBest[idx])
        else:
            raise Exception()
    return res

N, M, K = map(int, input().split())
ASBT = []
for m in range(M):
    ASBT.append(list(map(int, input().split())))
print(calc(N, M, K, ASBT))

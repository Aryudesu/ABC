N, K, P = [int(l) for l in input().split()]
CA = []
for n in range(N):
    tmp = tuple([int(l) for l in input().split()])
    CA.append(tmp)
dp = {tuple([0 for _ in range(K+1)]): 0}
INF = 10**13
result = INF

f = False
for idx in range(N):
    ca = CA[idx]
    new_dp = dict()
    for dat in dp:
        # データ取ってくる
        t = new_dp.get(dat, INF)
        # ある場合は既存と比較
        if dp[dat] <= t:
            new_dp[dat] = dp[dat]
        # コスト計算
        cost = dp[dat] + ca[0]
        # そのコスト未満で既にいいものがあればスルー
        if cost >= result:
            continue
        new_data = []
        tf = True
        # 各パラメタについて足してく
        for k in range(K):
            tmp = dat[k] + ca[k + 1]
            if tmp >= P:
                new_data.append(P)
            else:
                tf = False
                new_data.append(tmp)
        # パラメタをタプルにする
        tm = tuple(new_data)
        # そのパラメタ情報を取得
        t = new_dp.get(tm, INF)
        # 追加されている場合は比較
        if cost <= t:
            new_dp[tm] = cost
        # コストの更新
        if tf:
            f = True
            result = cost
    dp = new_dp
print(result if f else -1)

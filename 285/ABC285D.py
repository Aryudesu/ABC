def calc(ST):
    users = set()
    for S in ST:
        # すでに名義変更している場合無視
        if S in users:
            continue
        # 名義変更後取得
        T = ST.get(S)
        # 名義変更後が存在するなら
        if ST.get(T) is not None:
            # 変更前名義を保存しておく
            nodeS = set()
            # 変更前名義
            new_S = S
            while True:
                # 名義がループしているなら駄目
                if new_S in nodeS:
                    return "No"
                # 変更前名義保存
                nodeS.add(new_S)
                # 変更後名義取得
                new_T = ST.get(new_S)
                # 変更後名義のユーザについて
                new_S = ST.get(new_T)
                # 存在しない場合ループを抜ける
                if new_S is None:
                    break
                # すでに変更後なら大丈夫
                if new_S in users:
                    break
            for ns in nodeS:
                users.add(ns)
        else:
            users.add(S)
    return "Yes"


N = int(input())
ST = dict()
for n in range(N):
    s, t = [l for l in input().split()]
    ST[s] = t
print(calc(ST))

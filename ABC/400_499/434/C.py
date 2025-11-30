def calc(N, H, TLU):
    # 最大と最小
    fu = H
    fl = H
    # 時間
    now = 0
    for n in range(N):
        t, l, u = TLU[n]
        dt = t - now
        # 昇るとき
        if fu < u:
            # 範囲に入ることができるうちで最大
            newfu = min(u, fu + dt)
            # ドボン
            if fu + dt < l:
                return False
        else:
            # 下がるときは上界をuとする（下限は次で考慮）
            newfu = u
        if fl < l:
            # 昇る
            newfl = l
        else:
            newfl = max(l, fl - dt)
            # ドボン
            if fl - dt > u:
                return False
        fl, fu = newfl, newfu
        now = t
    return True




T = int(input())
for _ in range(T):
    N, H = map(int, input().split())
    TLU = [list(map(int, input().split())) for _ in range(N)]
    print("Yes" if calc(N, H, TLU) else "No")

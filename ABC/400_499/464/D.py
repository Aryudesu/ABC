def calc(N: int, S: str, X: list[int], Y: list[int])->int:
    # その日を変えなかった場合の嬉しさの最大値
    dp1 = [0] * N
    # その日を変えた場合の嬉しさの最大値
    dp2 = [0] * N
    dp2[0] -= X[0]
    for n in range(1, N):
        sp = S[n-1]
        sn = S[n]
        if sp == "R" and sn == "S":
            # 前日変えた場合か，変えなかった場合どちらかの最大値
            dp1[n] = max(Y[n-1] + dp1[n-1], dp2[n-1])
            # 今日変えても変化無し
            dp2[n] = max(dp1[n-1]-X[n], dp2[n-1]-X[n])
        elif sp == "S" and sn == "S":
            # 昨日変えた場合加算．昨日変えなかった場合そのまま
            dp1[n] = max(Y[n-1] + dp2[n-1], dp1[n-1])
            # 今日変えても変化無し
            dp2[n] = max(dp1[n-1]-X[n], dp2[n-1]-X[n])
        elif sp == "R" and sn == "R":
            # 変えなければ変化なし
            dp1[n] = max(dp1[n-1], dp2[n-1])
            # 今日変えると変化あり
            dp2[n] = max(Y[n-1] + dp1[n-1] - X[n], dp2[n-1] - X[n])
        elif sp == "S" and sn == "R":
            dp1[n] = max(dp1[n-1], dp2[n-1])
            # 今日変えると変化あり？
            dp2[n] = max(Y[n-1] + dp2[n-1] - X[n], dp1[n-1] - X[n])
    return max(dp1[-1], dp2[-1])


T = int(input())
result = []
for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    result.append(calc(N, S, X, Y))
for r in result:
    print(r)

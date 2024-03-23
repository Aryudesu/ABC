from atcoder.dsu import DSU

# 呼び出し
N, Q = [int(l) for l in input().split()]

# 入るボールの個数
all_num = N + Q
# ボール個数
ballNum = N

# boxes[代表値] = 箱の値
boxes = dict()
for n in range(N):
    boxes[n + 1] = n + 1

# balls[箱の値] = 代表値
ballData = dict()
for n in range(N):
    ballData[n + 1] = n + 1

result = []
balls = DSU(all_num + 1)
for q in range(Q):
    num, *query = [int(l) for l in input().split()]
    if num == 1:
        X, Y = query
        # 箱に入っているボールの代表値の取得
        x = ballData.get(X)
        y = ballData.get(Y)
        if (not x is None) and (not y is None):
            # 2つを結合
            balls.merge(x, y)
            # 結合後の代表値を取得
            ball_xl = balls.leader(x)
            # ラベルを貼る
            boxes[ball_xl] = X
            if ball_xl != y:
                boxes[y] = None
            else:
                boxes[x] = None
            # 箱に入っている代表値更新
            ballData[X] = ball_xl
            ballData[Y] = None
        elif x is None and (not y is None):
            # yの代表値の取得
            ball_yl = balls.leader(y)
            # ラベルを貼る
            boxes[ball_yl] = X
            # 箱に入っている代表値更新
            ballData[X] = ball_yl
            ballData[Y] = None
    elif num == 2:
        X = query[0]
        # Xに入っている代表値取得
        x = ballData.get(X)
        # Xに代表値が設定されている場合はマージ
        if not x is None:
            balls.merge(x, ballNum + 1)
        # 代表値取得
        ball_xl = balls.leader(ballNum + 1)
        # 箱の情報更新
        boxes[ball_xl] = X
        ballData[X] = ball_xl
        # ボールの個数を増やす
        ballNum += 1
    elif num == 3:
        X = query[0]
        # 代表値の取得
        ball_x = balls.leader(X)
        result.append(boxes.get(ball_x))
    else:
        raise Exception()
for r in result:
    print(r)

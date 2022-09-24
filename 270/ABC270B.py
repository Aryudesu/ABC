X, Y, Z = [int(l) for l in input().split()]
# 壁の内側にゴールがある場合
if abs(X) < abs(Y):
    print(abs(X))
# 壁の外側にゴールがある場合
elif X * Y > 0:
    # 壁と同じ方向にハンマーがある場合
    if Y * Z > 0:
        # 壁の向こう側にハンマーがある場合
        if abs(Y) < abs(Z):
            print(-1)
        else:
            # 壁の手前にハンマーがある場合
            print(abs(X))
    # 壁と反対方向にハンマーがある場合
    else:
        print(abs(X) + 2 * abs(Z))
# 壁と反対側にゴールがある場合
else:
    print(abs(X))

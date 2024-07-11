N = int(input())
A = [int(l) for l in input().split()]
R = [[0, 0]] * N
co = 0
l = -1
for a in A:
    # 何か入っている
    if l >= 0:
        # 最新のやつが同じ数
        if R[l][0] == a:
            # 個数1つ増やす
            R[l][1] += 1
            co += 1
            # 増やした結果kなら消える
            if R[l][1] == a:
                R[l] = [0, 0]
                co -= a
                l -= 1
        # 最新のやつが同じ数ではない
        else:
            # 新しく入れる
            R[l + 1] = [a, 1]
            l += 1
            co += 1
    else:
        l = 0
        R[0] = [a, 1]
        co += 1
    print(co)

N = int(input())
S = input()
# 1個前の結果と勝ち数
w = 1
d = 0
for n in range(1, N):
    # アオキが出した手
    s = S[n]
    # アオキが1手前に出した手
    ps = S[n - 1]
    new_w = w
    new_d = d
    # 前の手と同じ場合
    if ps == s:
        # 1個前の結果が勝利の場合は引き分けるしかない
        new_d = w
        # 1個前の結果が引き分けの場合は勝つしかない
        new_w = d + 1
    # アオキが1個前に出した手と異なる場合
    else:
        # 高橋が1個前に勝った場合に前に出した手
        pt = ""
        if ps == "R":
            pt = "P"
        elif ps == "P":
            pt = "S"
        elif ps == "S":
            pt = "R"
        # 高橋が今回勝つために出さないといけない手
        t = ""
        if s == "R":
            t = "P"
        elif s == "P":
            t = "S"
        elif s == "S":
            t = "R"
        # 前回出す手と異なる場合なので，(勝 → 勝), (分 → 分)で同じ手になることはない
        # 問題なのは(勝 → 分), (分 → 勝)になる場合
        # 分→勝になる場合
        if ps != t:
            new_w = d + 1
        # 勝→分になる場合
        elif pt != s:
            new_d = w
        # (勝 → 勝), (分 → 分)
        new_w = max([new_w, w + 1])
        new_d = max([new_d, d])
    w = new_w
    d = new_d
print(max([w, d]))

def calc(S, T):
    data = dict()
    c_data = set()
    t_at = 0
    chr = set(list("atcoder"))
    for s in S:
        data[s] = data.get(s, 0) + 1
        if s != "@":
            c_data.add(s)
    for t in T:
        # 後々何かと置き換える
        if t == "@":
            t_at += 1
            continue
        # 一致する文字がある場合
        tmp = data.get(t, 0)
        if tmp == 0:
            # atcoderの文字で置き換えれない場合ダメ
            if not t in chr:
                return False
            tmp_at = data.get("@", 0)
            # @上限個数の場合ダメ
            if tmp_at == 0:
                return False
            data["@"] = tmp_at - 1
        else:
            data[t] = tmp - 1
            if tmp == 1:
                c_data.remove(t)
    # T側の@について
    for c in c_data:
        # atcoderで置き換えられない場合ダメ
        if not c in chr:
            return False
        tmp = data.get(c)
        t_at -= tmp
        if t_at < 0:
            return False
    return True


S = input()
T = input()
print("Yes" if calc(S, T) else "No")

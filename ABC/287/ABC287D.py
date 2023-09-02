def is_eq(s, t):
    # 片方の文字が?か文字が同じであるか
    if s == "?" or t == "?":
        return True
    return s == t


def calc(S, T):
    lS = len(S)
    lT = len(T)
    # 初期段階で何個文字が不一致か
    Fnum = 0
    for l in range(lT):
        s = S[lS - 1 - l]
        t = T[lT - 1 - l]
        if is_eq(s, t):
            pass
        else:
            Fnum += 1
    print("No" if Fnum else "Yes")
    for l in range(lT):
        s = S[l]
        t = T[l]
        if is_eq(s, t):
            # 移動前が異なっている場合
            bs = S[lS - lT + l]
            bt = T[l]
            # 異なるポイント1つ減らす
            if not is_eq(bs, bt):
                Fnum -= 1
        else:
            # 前に移動したものがもう駄目だったらこれ以降全部駄目
            is_false = True
            Fnum += 1
        print("No" if Fnum else "Yes")


S = input()
T = input()
calc(S, T)

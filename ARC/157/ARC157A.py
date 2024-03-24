def calc(N, A, B, C, D):
    # XYとYXが同じ個数の場合
    if B == C:
        # XYもYXも存在しない場合
        if B == 0:
            # XXとYYどちらかしか存在できない
            if A == 0 or D == 0:
                return True
            else:
                return False
        else:
            # 存在するならOK
            return True
    # XYの方がYXより1個多い場合，Xで始まりYで終わっている
    elif B + 1 == C:
        return True
    # YXの方がXYより1個多い場合，Yで始まりXで終わっている
    elif B == C + 1:
        return True
    # それら以外はできない
    return False


N, A, B, C, D = [int(l) for l in input().split()]
print("Yes" if calc(N, A, B, C, D) else "No")

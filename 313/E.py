# 終わらないパターン
def check1(S):
    f = False
    for s in S:
        if s != "1":
            if f:
                return False
            f = True
        else:
            f = False
    return True


def check2(S):
    pass


N = int(input())
S = input()

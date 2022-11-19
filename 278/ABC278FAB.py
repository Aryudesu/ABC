from functools import lru_cache
INFTY = 10 ** 10


def calc_value(turn):
    """評価関数"""
    # 自分のターンで手詰まりなら負けなので-1，相手のターンで手詰まりなら勝ちなので1を返す
    return -1 if turn else 1


@lru_cache(maxsize=2**16)
def alpha_beta(prev, turn, choise, N, alpha, beta):
    # 次に選べる手
    can_choise = set()
    for i in range(N):
        t = 1 << i
        c = choise & t
        if c == 0 and S[prev][1] == S[i][0]:
            can_choise.add(i)

    # 手詰まりの場合
    if not len(can_choise):
        # その手での評価を返す
        return calc_value(turn)

    # 先手の場合
    if turn:
        score = alpha
        for c in can_choise:
            t = 1 << c
            # 総当り
            s_tmp = alpha_beta(c, not turn, choise | t, N, score, beta)
            if s_tmp > score:
                score = s_tmp
            if score >= beta:
                break
    # 後手の場合
    else:
        score = beta
        for c in can_choise:
            t = 1 << c
            s_tmp = alpha_beta(c, not turn, choise | t, N, alpha, score)
            if s_tmp < score:
                score = s_tmp
            if score <= alpha:
                break
    return score


N = int(input())
S = []
for n in range(N):
    tmp = input()
    S.append([tmp[0], tmp[-1]])
# まず先手が選ぶ
res = -1
for idx in range(N):
    tmp = alpha_beta(idx, False, 2 ** idx, N, -INFTY, INFTY)
    if res < tmp:
        res = tmp
print("First" if res > 0 else "Second")

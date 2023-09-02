from functools import lru_cache


@lru_cache(maxsize=2**16)
def min_max(prev, turn, choise, N):
    # 全部選んでしまった場合
    if choise == ((1 << N) - 1):
        # 先手の場合-1，後手の場合1を返す
        return -1 if turn else 1
    # 先手の場合
    if turn:
        score = -1
        for i in range(N):
            # 総当り
            t = 1 << i
            c = choise & t
            # 選んでない場合で，しりとりの条件に即しているなら
            if c == 0 and S[prev][1] == S[i][0]:
                s_tmp = min_max(i, not turn, choise | t, N)
                if s_tmp > score:
                    score = s_tmp
    # 後手の場合
    else:
        score = 1
        for i in range(N):
            t = 1 << i
            c = choise & t
            if c == 0 and S[prev][1] == S[i][0]:
                s_tmp = min_max(i, not turn, choise | t, N)
                if s_tmp < score:
                    score = s_tmp
    return score


N = int(input())
S = []
for n in range(N):
    tmp = input()
    S.append([tmp[0], tmp[-1]])
# まず先手が選ぶ
res = -1
for idx in range(N):
    tmp = min_max(idx, False, 2 ** idx, N)
    if res < tmp:
        res = tmp
print("First" if res == 1 else "Second")

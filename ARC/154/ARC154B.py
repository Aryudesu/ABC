def lgest_end(N, S, T):
    result = 0
    lidx = N - 1
    for n in range(N):
        # Tの末尾から探索
        ls = 0
        for m in range(N):
            # Sの末尾から探索
            if n + m == N:
                break
            if T[N - n - m - 1] == S[N - m - 1]:
                ls += 1
            else:
                break
        if result < ls:
            lidx = N - n - ls
            result = ls
    return result, lidx


def lgest_st(N, S, T, l):
    for n in range(N):
        # Sの先頭から探索
        for m in range(N):
            # Tの先頭から探索
            if n + m == N - l:
                return N - n
            if S[n + m] != T[m]:
                break
    return N - l


def check(N, S, T):
    d = dict()
    for idx in range(N):
        s = S[idx]
        t = T[idx]
        tmp = d.get(s, 0)
        d[s] = tmp + 1
        tmp = d.get(t, 0)
        d[t] = tmp - 1
    for k, v in d.items():
        if v > 0:
            return False
    return True


def calc(N, S, T):
    if not check(N, S, T):
        print('-1')
        return
    lng_same1, lidx = lgest_end(N, S, T)
    if lidx == 0:
        # 末尾のものが先頭から始まっている場合
        print(N - lng_same1)
    else:
        # 先頭から始まっている文字数 - 末尾が一致する最長
        result = lgest_st(N, S, T, lng_same1)
        print(result)
    return


N = int(input())
S = input()
T = input()

calc(N, S, T)

def yakusu(L):
    res = []
    for i in range(1, L+1):
        if L%i == 0:
            res.append(i)
    return res


def isTen(s):
    if len(s) == 1:
        return False
    if s[0] != '1':
        return False
    for n in range(1, len(s)):
        if s[n] != '0':
            return False
    return True


def calcKaiMax(T, L):
    yaku = yakusu(L)
    # 約数文字ごとに文字を分割
    max = 0
    # 1桁の場合はそれが答え
    if len(T) == 1:
        if max <= int(T):
            max = int(T)
    # 素数桁の場合は同じ文字連続しないといけない
    elif len(yaku) == 2:
        # 頭が1の時は1が連続するか9が連続
        if T[0] == '1':
            a = ''
            for n in range(len(T)):
                a += '1'
            if int(a) <= int(T):
                max = int(a)
            else:
                a = ''
                for n in range(len(T) - 1):
                    a += '9'
                if max <= int(a):
                    max = int(a)
        else:
            # 頭が1で無い場合はその数が連続するか1つ下の数が連続しないといけない
            a = ''
            for n in range(len(T)):
                a += T[0]
            tmp = int(a)
            tmp2 = int(T)
            if tmp <= tmp2:
                max = tmp
            else:
                a = ''
                b = str(int(T[0]) - 1)
                for n in range(len(T)):
                    a += b
                tmp = int(a)
                max = tmp
    # 合成数桁の場合
    else:
        for y in yaku:
            # 長さがもとの長さの場合は除外
            if y == L:
                continue
            S = [T[i:i+y] for i in range(0,len(T), y)]
            tmp = int(T)
            # 10のべき乗の場合は9が連続する
            if not isTen(S[0]):
                a = ''
                for s in S:
                    a += S[0]
                tmp2 = int(a)
                if tmp2 <= tmp:
                    if max < tmp2:
                        max = tmp2
                else:
                    tmp3 = str(int(S[0]) - 1)
                    a = ''
                    for s in S:
                        a += tmp3
                    if max <= int(a):
                        max = int(a)
            else:
                a = ''
                for s in S:
                    a += S[0]
                if int(a) <= int(T):
                    if max <= int(a):
                        max = int(a)
                else:
                    a = ''
                    for n in range(len(T) - 1):
                        a += '9'
                    if max <= int(a):
                        max = int(a)
    return max


N = int(input())
for n in range(N):
    T = input()
    L = len(T)
    max = calcKaiMax(T, L)
    print(max)

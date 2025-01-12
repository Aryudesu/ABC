# ヘビ数かどうか
def isSnake(snum):
    h = int(snum[0])
    for i in range(1, len(snum)):
        if h <= int(snum[i]):
            return False
    return True

# 頭と桁数固定でnum以下のヘビ数の個数計算
def calc_h(h, l, snum):
    result = 0
    for i in range(1, l):
        n = int(snum[i])
        if n >= h:
            result += h ** (l - i)
            return result
        result += h ** (l - i - 1) * min([h - 1, n])
    # if isSnake(snum):
    result += 1
    # print(h, l, snum, result)
    return result

# 頭固定で長さ指定のヘビ数の個数計算
def calc_len(h, l):
    return h ** (l - 1)

# num以下のヘビ数の個数計算
def calc(num):
    s = str(num)
    sh = int(s[0])
    sl = len(s)
    result = 0
    for h in range(1, sh):
        result += calc_len(h, sl)
    for l in range(2, sl):
        for h in range(1, 10):
            result += calc_len(h, l)
    # print(result)
    result += calc_h(sh, sl, s)
    # print(result)
    return result

L, R = [int(l) for l in input().split()]
l = calc(L)
r = calc(R)
m = 0
# print(l, r)
if isSnake(str(L)):
    m = 1
print(r - l + m)

# ミノ，フィールド状態，置く位置、回転
def is_ok(p, F, x, y, n):
    for dx in range(4):
        for dy in range(4):
            if n == 0:
                a = dx
                b = dy
            elif n == 1:
                a = 3 - dy
                b = dx
            elif n == 2:
                a = 3 - dx
                b = 3 - dy
            elif n == 3:
                a = dy
                b = 3 - dx
            # '#'で
            if p[a][b] == "#":
                # 枠内に入っていて
                if x + dx >= 0 and x + dx <= 3 and y + dy >= 0 and y + dy <= 3:
                    # すでに置かれていたらダメ
                    if F[x + dx][y + dy] == "#":
                        return False
                else:
                    # 枠外だとダメ
                    return False
                F[x + dx][y + dy] = "#"
    # 最後まで大丈夫ならOK
    return True


def initField():
    return [[".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]


def copyField(F):
    res = initField()
    for i in range(4):
        for j in range(4):
            res[i][j] = F[i][j]
    return res


def printField(F, N):
    # print(N)
    for f in F:
        print("".join(f))


def is_all(F):
    for i in range(4):
        for j in range(4):
            if F[i][j] != "#":
                return False
    return True


def calc(P, F, N):
    # printField(F, N)
    for a in range(10):
        for b in range(10):
            for c in range(4):
                f = copyField(F)
                if is_ok(P[N], f, a - 3, b - 3, c):
                    if N == 0:
                        if is_all(f):
                            return True
                    elif calc(P, f, N - 1):
                        return True
    return False


P = []
for i in range(3):
    tmp = []
    for j in range(4):
        tmp.append(list(input()))
    P.append(tmp)
F = initField()
res = calc(P, F, 2)
print("Yes" if res else "No")

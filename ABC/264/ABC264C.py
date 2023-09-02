# 縦について検証
def checkR(A, B, H1, W1, H2, W2, h1, w1, w2):
    r = 1
    if H2 > 1:
        for h in range(h1 + 1, H1):
            if A[h][w1] == B[r][w2]:
                r += 1
                if r == H2:
                    return True
        return False
    return True 


# Bの横の列について検証します
def check(A, B, H1, W1, H2, W2, h1, w1):
    c = 1
    # 最初のやつ全走査
    if not checkR(A, B, H1, W1, H2, W2, h1, w1, 0):
        return False
    if W2 > 1:
        # Aの指定の行を全走査
        for w in range(w1 + 1, W1):
            # 対象について同じものがあれば縦について検証
            if A[h1][w] == B[0][c]:
                if checkR(A, B, H1, W1, H2, W2, h1, w, c):
                    c += 1
                    if c == W2:
                        return True
        return False
    return True


def search(A, B, H1, W1, H2, W2):
    # Bの左上にあたる数字を見つける
    if H1 > H2:
        for h1 in range(H1 - H2 + 1):
            if W1 > W2:
                for w1 in range(W1 - W2 + 1):
                    if A[h1][w1] == B[0][0]:
                        if check(A, B, H1, W1, H2, W2, h1, w1):
                            return True
            else:
                if A[h1][0] == B[0][0]:
                    if check(A, B, H1, W1, H2, W2, h1, 0):
                        return True
    else:
        if W1 > W2:
            for w1 in range(W1 - W2 + 1):
                if A[0][w1] == B[0][0]:
                    if check(A, B, H1, W1, H2, W2, 0, w1):
                        return True
        else:
            if A[0][0] == B[0][0]:
                if check(A, B, H1, W1, H2, W2, 0, 0):
                    return True
    return False


H1, W1 = [int(l) for l in input().split()]
A = []
for h in range(H1):
    A.append([int(l) for l in input().split()])


H2, W2 = [int(l) for l in input().split()]
B = []
for h in range(H2):
    B.append([int(l) for l in input().split()])


if search(A, B, H1, W1, H2, W2):
    print('Yes')
else:
    print('No')

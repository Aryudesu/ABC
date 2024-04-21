A = []
A.append([int(l) for l in input().split()])
A.append([int(l) for l in input().split()])
A.append([int(l) for l in input().split()])

# ===================評価値計算
def isThree(field):
    # 縦
    if field[0][0] == field[0][1] and field[0][1] == field[0][2]:
        return field[0][0]
    if field[1][0] == field[1][1] and field[1][1] == field[1][2]:
        return field[1][0]
    if field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        return field[2][0]
    # 横
    if field[0][0] == field[1][0] and field[1][0] == field[2][0]:
        return field[0][0]
    if field[0][1] == field[1][1] and field[1][1] == field[2][1]:
        return field[0][1]
    if field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        return field[0][2]
    # 斜
    if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        return field[0][0]
    if field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        return field[0][2]
    return 0

def isMax(field):
    for i in range(3):
        for j in range(3):
            if field[i][j] == 0:
                return False
    return True

def judge(field, sc):
    three = isThree(field)
    if three != 0:
        return True, three
    ism = isMax(field)
    if ism:
        return True, sc
    return False, 0


MAX = 10 ** 18
def minMax(field, turn, sc, alpha, beta):
    """minmax法で評価値を計算します"""
    res, scr = judge(field, sc)
    if res:
        return scr
    if turn:
        maxScore = alpha
        for i in range(3):
            for j in range(3):
                if field[i][j] == 0:
                    field[i][j] = 1
                    score = minMax(field, not turn, sc + A[i][j], maxScore, beta)
                    field[i][j] = 0
                    if score > maxScore:
                        maxScore = score
                    if maxScore >= beta:
                        return maxScore
        return maxScore
    else:
        minScore = beta
        for i in range(3):
            for j in range(3):
                if field[i][j] == 0:
                    field[i][j] = -1
                    score = minMax(field, not turn, sc - A[i][j], alpha, minScore)
                    field[i][j] = 0
                    if score < minScore:
                        minScore = score
                    if alpha >= minScore:
                        return minScore
        return minScore

Field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
score = minMax(Field, True, 0, -MAX, MAX)
print("Takahashi" if score > 0 else "Aoki")

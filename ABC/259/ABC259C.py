def calcA(S):
    res = []
    nc = S[0]
    co = 0
    for s in S:
        if s == nc:
            co += 1
        else:
            res.append([nc, co])
            nc = s
            co = 1
    res.append([nc, co])
    return res


def calc(A, B):
    if len(A) != len(B):
        return False
    lA = len(A)
    for i in range(lA):
        # 文字が同じ
        if A[i][0] == B[i][0]:
            # 文字数が異なる場合
            if A[i][1] != B[i][1]:
                # Aの文字列のほうが多かったら駄目
                if A[i][1] > B[i][1]:
                    return False
                # Aが1文字でBが2文字以上連続だと駄目
                if A[i][1] == 1 and B[i][1] >= 2:
                    return False
        # 文字が異なる場合駄目
        else:
            return False
    return True


S = input()
A = calcA(S)
T = input()
B = calcA(T)
if calc(A, B):
    print("Yes")
else:
    print("No")

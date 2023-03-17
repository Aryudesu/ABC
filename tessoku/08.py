def calc_sum_array(H, W, X):
    result = []
    ST = []
    tmp = 0
    for w in range(W):
        tmp += X[0][w]
        ST.append(tmp)
    result.append(ST)
    for h in range(1, H):
        tmp = 0
        ST = []
        for w in range(W):
            tmp += X[h][w]
            ST.append(tmp + result[h - 1][w])
        result.append(ST)
    return result


def get_sum(Y, X, S):
    if Y > 0 and X > 0:
        # print(X, Y, S[Y-1][X-1])
        return S[Y-1][X-1]
    return 0


def calc(A, B, C, D, S):
    result = get_sum(C, D, S)
    result -= get_sum(A-1, D, S)
    result -= get_sum(C, B-1, S)
    result += get_sum(A-1, B-1, S)
    return result


H, W = [int(l) for l in input().split()]
X = []
for h in range(H):
    X.append([int(l) for l in input().split()])
S = calc_sum_array(H, W, X)
result = []
Q = int(input())
for q in range(Q):
    A, B, C, D = [int(l) for l in input().split()]
    result.append(calc(A, B, C, D, S))
for r in result:
    print(r)

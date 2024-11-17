def calc(N, M, X, A, E):
    a_sum = 0
    co = 0
    e = 0
    for i in range(M - 1, -1, -1):
        a_sum += A[i]
        co += A[i] - 1
        e += E[i]
        if co > e:
            return -1
    if a_sum != N:
        return -1
    # 結果
    result = 0
    # 見てる個数についてループ
    for ap in range(M):
        # 動かせる個数
        epnum = 0
        # 空きマスの方が少なければ空きマス分動かす
        if E[ap] <= A[ap] - 1:
            epnum = E[ap]
        # 空きマスの方が多ければ動かせるだけ動かす
        else:
            epnum = A[ap] - 1
        result += (epnum * (epnum + 1)) // 2
        if A[ap] - 1 > E[ap]:
            A[ap + 1] += A[ap] - E[ap] - 1
            result += (A[ap] - E[ap] - 1) * (X[ap + 1] - X[ap])
    return result



N, M = [int(l) for l in input().split()]
# 置いてるマス
tmpX = [int(l) - 1 for l in input().split()]
# 置いてる個数
tmpA = [int(l) for l in input().split()]
XA = []
for m in range(M):
    XA.append([tmpX[m], tmpA[m]])
XA.sort()
X = []
A = []
for x, a in XA:
    X.append(x)
    A.append(a)
p = N
c = 0
# X[i] ~ X[i + 1]間に開いてるマスの個数
E = []
for i in range(M):
    idx = -1 - i
    c = p - X[idx] - 1
    E.append(c)
    p = X[idx]
E.reverse()
print(calc(N, M, X, A, E))

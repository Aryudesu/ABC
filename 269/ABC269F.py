def calcC(V, W, M):
    X = (V+1) // 2
    Y = (W+1) // 2
    X = X if X > 0 else 0
    Y = Y if Y > 0 else 0
    XR = X**2
    YR = ((Y - 1) * Y)//2
    res = XR * Y + (2 * M) * YR * X
    # print("V, W, X, Y, XR, YR, res", V, W, X, Y, XR, YR, res)
    return res


N, M = [int(l) for l in input().split()]
Q = int(input())
res = []
for q in range(Q):
    A, B, C, D = [int(l) for l in input().split()]
    # 右下 + 左上 - 右上 - 左下
    TL0 = calcC(D, B, M) + calcC(C-1, A-1, M) - calcC(D, A-1, M) - calcC(C-1, B, M)
    TL1 = calcC(D-1, B-1, M) + calcC(C-2, A-2, M) - calcC(D-1, A-2, M) - calcC(C-2, B-1, M)
    s = TL0
    if TL1:
        A_ = (A)//2
        B_ = (B)//2
        C_ = (C)//2
        D_ = (D)//2
        A_ = A_ if A_ > 0 else 0
        B_ = B_ if B_ > 0 else 0
        C_ = C_ if C_ > 0 else 0
        D_ = D_ if D_ > 0 else 0
        s += TL1 + (M + 1) * (B_ - A_ + 1) * (D_ - C_ + 1)
    res.append(s)
for r in res:
    print(r)

def calc(N: int, X: int, Y: int, A: list[int]) -> int:
    # a_0 + b_0 = A[0]   Xa_0 + Yb_0 = K
    # (Y-X)b_0 = K - XA[0]
    # 少なくともK - XA[0]は(Y-X)の倍数である必要がある
    # → XA[0]を(Y-X)で割ったあまりが全部同じである必要がある
    # (K - XA[n])/(Y-X)を考えて
    # 0 <= b_0 <= A[0]
    # 0 <= b_{N-1} <= A[-1]
    # の2つを見れば良さそう
    # b_0の最大値(=A[0])に対してA[-1]が対応できるか？という問題になる？
    M = Y - X
    data = set()
    for a in A:
        data.add((a * X) % M)
    if len(data) > 1:
        return -1
    K = A[0] * Y
    if K - A[-1] * X < 0:
        return -1
    result = 0
    for a in A:
        result += (K - a*X)//(Y-X)
    return result
    


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(calc(N, X, Y, A))

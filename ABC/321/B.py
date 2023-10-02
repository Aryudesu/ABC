def calc(N, X, A):
    A.sort()
    s = 0
    for i in range(1, N - 2):
        s += A[i]
    # 最小値更新で解決する場合
    if X - s <= A[0]:
        return 0
    # 最大値2つあればできる場合
    if X - s == A[-1]:
        return A[-1]
    # 最大値更新しないとできない場合
    if X - s > A[-1]:
        return -1
    return X - s


N, X = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(calc(N, X, A))

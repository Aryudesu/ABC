from bisect import bisect_right, bisect_left

def calc(N, A, Aset, X, Y):
    # リストの中のX未満の個数
    if not X in Aset and Y == 1:
        return X
    xlt = bisect_left(A, X)
    d = 1
    if X in Aset:
        d = 0
    # リスト最大未満のうちリストに含まれないX以上のものの個数がc
    c = A[-1] - X + 1 - (N - xlt)
    # それですら達しないとき
    if c < Y:
        d = Y - c
        return A[-1] + d
    left = X
    right = A[-1]
    while abs(right - left) > 1:
        mid = (right + left) //2
        # リストの中のmid未満の個数
        midlqt = bisect_right(A, mid)
        # X以上mid以下の個数計算
        c = mid - X - (midlqt - xlt)
        if c == Y:
            return mid
        if c > Y:
            right = mid
        else:
            left = mid
    return left


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
Aset = set(A)
XY = []
for q in range(Q):
    x, y = map(int, input().split())
    res = calc(N, A, Aset, x, y)
    print(res)

H, W, Q = map(int, input().split())
for _ in range(Q):
    n, d = map(int, input().split())
    if n == 1:
        print(d * W)
        H -= d
    elif n == 2:
        print(d * H)
        W -= d
    else:
        raise ValueError()

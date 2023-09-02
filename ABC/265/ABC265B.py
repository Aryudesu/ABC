def calc(N, M, T, A, XY):
    t = T
    for n in range(N - 1):
        # print(t)
        b = XY.get(n + 1, 0)
        t += b
        t -= A[n]
        if t <= 0:
            return False
    # print(t)
    return True


N, M, T = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
XY = dict()
for m in range(M):
    X, Y = [int(l) for l in input().split()]
    XY[X] = Y

if calc(N, M, T, A, XY):
    print('Yes')
else:
    print('No')

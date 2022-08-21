X, Y, N = [int(l) for l in input().split()]

if 3 * X < Y:
    print(N * X)
else:
    print(X * (N % 3) + Y * (N//3))

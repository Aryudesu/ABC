N, X, Y = [int(l) for l in input().split()]
X, Y = abs(X), abs(Y)
if X + Y > N:
    print("No")
else:
    if (N - X - Y) % 2 == 0:
        print("Yes")
    else:
        print("No")

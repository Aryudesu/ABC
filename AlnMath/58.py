N, X, Y = [int(l) for l in input().split()]
print("No" if (N - X - Y) % 2 or N < X + Y else "Yes")

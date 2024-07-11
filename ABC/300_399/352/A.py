N, X, Y, Z = [int(l) for l in input().split()]
x, y = min([X, Y]), max([X, Y])
print("Yes" if x <= Z and Z <= y else "No")


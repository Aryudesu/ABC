N, X, Y = [int(l) for l in input().split()]
r = 1
b = 0
for n in range(N - 1):
    r, b = r + b + r * X, (b + r * X) * Y
print(b)

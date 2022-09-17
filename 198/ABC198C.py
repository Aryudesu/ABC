import math

R, X, Y = [int(l) for l in input().split()]
D = (X**2 + Y**2) ** 0.5
if D > R:
    D = math.ceil(D)
    print(D//R + (1 if D % R else 0))
elif D == R:
    print(1)
else:
    print(2)

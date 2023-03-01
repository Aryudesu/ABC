import math

N, X, Y = [int(l) for l in input().split()]
print((N//X) + (N//Y) - (N * math.gcd(X, Y))//(X*Y))

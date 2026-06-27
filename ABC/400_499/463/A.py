from math import gcd

X, Y = map(int, input().split())
G = gcd(X, Y)
X = X//G
Y = Y//G
print("Yes" if (X, Y) == (16, 9) else "No")

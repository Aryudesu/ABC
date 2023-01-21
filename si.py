import math

a, b, c = [int(l) for l in input().split()]
result = (c - a - b) ** 2 > 4 * a * b and c - a - b > 0
print("Yes" if result else "No")

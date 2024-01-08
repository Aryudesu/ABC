import math

a, b, c = [int(l) for l in input().split()]
print("Yes" if a < c**b else "No")

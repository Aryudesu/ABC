import math

a, b, d = [int(l) for l in input().split()]
na = a * math.cos(math.pi * (d / 180)) - b * math.sin(math.pi * (d / 180))
nb = a * math.sin(math.pi * (d / 180)) + b * math.cos(math.pi * (d / 180))
print(na, nb)

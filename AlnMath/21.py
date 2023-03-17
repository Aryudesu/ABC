import math

n, r = [int(l) for l in input().split()]
print(math.factorial(n)//(math.factorial(r) * math.factorial(n-r)))

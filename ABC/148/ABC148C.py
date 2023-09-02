import math
A, B = [int(l) for l in input().split()]
print((A*B)//math.gcd(A, B))

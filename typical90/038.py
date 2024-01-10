import math

A, B = [int(l) for l in input().split()]
g = math.gcd(A, B)
result = (B * A)//g
print("Large" if result > 10 ** 18 else result)

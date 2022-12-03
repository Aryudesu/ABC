import math

A, B = [int(l) for l in input().split()]
g = 1
k = int((A/(2 * B)) ** (2/3) - 1)
if k != 0 and k != -1 and k != -2:
    s = B * (k-1) + A/math.sqrt(k)
    t = B * k + A/math.sqrt(k + 1)
    u = B * (k + 1) + A/math.sqrt(k + 2)
    result = min([s, t, u])
elif k == -2:
    s = B * (k-1) + A/math.sqrt(k)
    t = B * k + A/math.sqrt(k + 1)
    result = min([s, t])
elif k == -1:
    s = B * (k-1) + A/math.sqrt(k)
    u = B * (k + 1) + A/math.sqrt(k + 2)
    result = min([s, u])
elif k == 0:
    t = B * k + A/math.sqrt(k + 1)
    u = B * (k + 1) + A/math.sqrt(k + 2)
    result = min([t, u])
print(result)

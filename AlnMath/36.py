import math

A, B, H, M = [int(l) for l in input().split()]
HA = 12 * 60
MA = 60
HM = H * 60 + M
res = (A ** 2 + B ** 2 - 2 * A * B * math.cos((HM / HA - M / MA) * 2 * math.pi)) ** 0.5
print(res)

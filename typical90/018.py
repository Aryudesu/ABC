import math

T = int(input())
L, X, Y = [int(l) for l in input().split()]
result = []
Q = int(input())
for _ in range(Q):
    E = int(input())
    t = (2 * math.pi * E) / T
    now_X = 0
    now_Y = -L * math.sin(t)/2
    now_Z = -L*(math.cos(t) - 1)/2
    a = math.sqrt((now_X - X) ** 2 + (now_Y - Y) ** 2)
    res = 360 * math.atan2(now_Z, a)/(2*math.pi)
    result.append(res)
for r in result:
    print(r)

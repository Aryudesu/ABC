from math import gcd

N = int(input())
T = list(map(int, input().split()))
T.reverse()
now = 1
for t in T:
    g = gcd(t, now)
    if t % now == 0:
        now = t

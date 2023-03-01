import math

N = 20240101
mu = [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0]
lm = len(mu) - 1
res = 0
for m in range(1, lm):
    tmp = 0
    tmp += (1/(math.log(N)))
    tmp += 2 * m * (1/(math.log(N)) ** 2)
    res += mu[m] * tmp * int(N**(1/m))
print(res)

import math
import sys
from itertools import permutations


def calcKetasu(a, b):
    return int(b * math.log10(a)) + 1

sys.set_int_max_str_digits(10000000)
data = [5, 4, 9]
result = 0
maxData = []
aftFlg = False
for dat in permutations(data):
    tmp = calcKetasu(dat[0], dat[1]**dat[2])
    if result < tmp:
        aftFlg = True
        result = tmp
        maxData = dat
    tmp = calcKetasu(dat[0]**dat[1], dat[2])
    if result < tmp:
        aftFlg = False
        result = tmp
        maxData = dat
print(result)
print(maxData)
print(aftFlg)

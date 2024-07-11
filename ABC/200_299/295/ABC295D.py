d = [1]+[0]*1023
e = r = 0
for s in input():
    e ^= 1 << int(s)
    r += d[e]
    d[e] += 1
print(r)

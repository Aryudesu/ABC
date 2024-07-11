N, M = [int(l) for l in input().split()]
S = input()
onum = 0
tnum = 0
o, t = 0, 0
for s in S:
    if s == "1":
        o += 1
    if s == "2":
        t += 1
        o += 1
    if s == "0":
        if onum < o:
            onum = o
        if tnum < t:
            tnum = t
        o, t = 0, 0
if onum < o:
    onum = o
if tnum < t:
    tnum = t
result = tnum
if onum - M > tnum:
    result = onum - M
print(result)

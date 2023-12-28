N = int(input())
B = [int(l) for l in input().split()]
R = [int(l) for l in input().split()]
Bdata, Rdata = dict(), dict()
RMax , BMax = 0, 0
for r in R:
    Rdata[r] = Rdata.get(r, 0) + 1
    if RMax < r:
        RMax = r
for b in B:
    Bdata[b] = Bdata.get(b, 0) + 1
    if BMax < b:
        BMax = b

result = 0
for i in range(RMax + BMax + 1):
    count = 0
    for b in Bdata:
        count += Rdata.get(i - b, 0) * Bdata.get(b, 0)
    result += i * (count / (N**2))
print(result)

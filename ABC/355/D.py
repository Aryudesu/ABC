N = int(input())
LR = []
data = []
for n in range(N):
    l, r = [int(l) for l in input().split()]
    data.append((l, -1))
    data.append((r, +1))
data.sort()
idx = 0
c = 0
result = 0
# print(data)
for dat in data:
    num = dat[0]
    t = dat[1]
    if idx < num:
        idx = num
    c -= t
    if c > 0 and t < 0:
        result += c - 1
print(result)

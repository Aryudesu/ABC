N = int(input())
A = [int(l) for l in input().split()]
data = []
deg = 0
for a in A:
    deg = (deg + a) % 360
    data.append(deg)
data.sort()
data.append(360)
result = data[0]
prev = data[0]
for dat in data:
    tmp = dat - prev
    result = max(result, tmp)
    prev = dat
print(result)

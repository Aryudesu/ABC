INF = 10 ** 9
N = int(input())
data = dict()
for n in range(N):
    a, c = [int(l) for l in input().split()]
    tmp = data.get(c, INF)
    data[c] = min([tmp, a])

dat = []
for k in data:
    dat.append(data[k])
print(max(dat))

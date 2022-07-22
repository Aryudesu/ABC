import math

N, K = [int(l) for l in input().split()]
light = [int(l) for l in input().split()]
pc = []
lc = []
for n in range(N):
    if (n+1 in light):
        lc.append([int(l) for l in input().split()])
    else:
        pc.append([int(l) for l in input().split()])

inf = (((10**5)*2)**2)*2
max = 0
for p in range(N-K):
    min = inf
    for l in range(K):
        tmp = (pc[p][0] - lc[l][0])**2 + (pc[p][1] - lc[l][1])**2
        if min > tmp:
            min = tmp
    if max < min:
        max = min
print(math.sqrt(max))

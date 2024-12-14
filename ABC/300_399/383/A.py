N = int(input())
w = 0
pt = 0
for n in range(N):
    t, v = [int(l) for l in input().split()]
    w = max([v, w + (pt - t) + v])
    pt = t
print(w)

import bisect

N, M, K = [int(l) for l in input().split()]
AB = [[int(l) for l in input().split()] for _ in range(N)]
CD = [[int(l) for l in input().split()] for _ in range(M)]
ng = 0
ok = 1
for _ in range(100):
    x = (ng + ok) / 2
    z = x / (1-x)
    v = [cd[0] - cd[1] * z for cd in CD]
    v.sort()
    num = 0
    for i in range(N):
        w = AB[i][0] - AB[i][1] * z
        num += M - bisect.bisect_left(v, -w)
    if num < K:
        ok = x
    else:
        ng = x
print(ok * 100)

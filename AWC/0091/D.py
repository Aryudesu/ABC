from atcoder.dsu import DSU

N, Q, K = map(int, input().split())
times = set()
times.add(0)
gaitouData = []
for n in range(N):
    a, d = map(int, input().split())
    if d == 0:
        if a > K:
            t = 10**9 + 5
        else:
            t = 0
    else:
        t = (a - K + d - 1)//d
    gaitouData.append(t)
    times.add(t)
times = sorted(times)
timeData = []
print(gaitouData)
dsu = DSU(N)
kuraiLeaders = set()
for n in range(N):
    if gaitouData[n] == 0:
        kuraiLeaders.add(n)
        if n - 1 >= 0:
            if gaitouData[n-1] == 0:
                kuraiLeaders.discard(n-1)
                nl = dsu.merge(n-1, n)
                kuraiLeaders.add(nl)
for t in times:
    print(t)
print(kuraiLeaders)
for _ in range(Q):
    t = input()

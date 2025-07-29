N, L = [int(l) for l in input().split()]
INF = 10**10
Wmax, Emin = 0, 10**10
for n in range(N):
    a, b = input().split()
    if b == "W":
        Wmax = max(Wmax, int(a))
    elif b == "E":
        Emin = min(Emin, int(a))
print(max(Wmax, 0 if Emin == INF else L - Emin))

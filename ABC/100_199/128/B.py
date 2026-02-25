N = int(input())
data = []
for n in range(N):
    S, P = input().split()
    P = int(P)
    data.append((S, -P, n + 1))
data.sort()
for s, p, n in data:
    print(n)

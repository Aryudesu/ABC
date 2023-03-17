D = int(input())
N = int(input())
day = [0] * D
for n in range(N):
    L, R = [int(l) for l in input().split()]
    day[L - 1] += 1
    if R < D:
        day[R] -= 1
s = 0
for d in day:
    s += d
    print(s)

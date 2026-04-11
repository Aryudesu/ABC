from fractions import Fraction

N, M = map(int, input().split())
V = list(map(int, input().split()))
data = []
for m in range(M):
    d, t = map(int, input().split())
    data.append((Fraction(d, t), t, d))
data.sort(reverse=True)
V.sort(reverse=True)
vidx = 0
for f, t, d in data:
    if V[vidx] * t >= d:
        vidx += 1
    if vidx >= N:
        break
print(vidx)

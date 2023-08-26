N = int(input())
P = [int(l) for l in input().split()]
mi = 0
for i in range(N):
    if P[mi] <= P[i]:
        mi = i
if mi:
    print(P[mi] - P[0] + 1)
else:
    print(0)

N, M = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
L = [int(l) for l in input().split()]
D = [int(l) for l in input().split()]
LD = []
for i in range(M):
    LD.append((L[i], -D[i]))
P.sort()
LD.sort()
result = 0

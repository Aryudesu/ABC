N, Q = [int(l) for l in input().split()]
A = []
for n in range(N):
    A.append([int(l) for l in input().split()])
res = []
for q in range(Q):
    s, t = [int(l) for l in input().split()]
    print(A[s-1][t])

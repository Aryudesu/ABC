H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
B = []
for w in range(W):
    tmp = []
    for h in range(H):
        tmp.append(A[h][w])
    B.append(tmp)
for b in B:
    print(*b)


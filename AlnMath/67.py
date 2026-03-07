H, W = [int(l) for l in input().split()]
A = [[int(l) for l in input().split()] for _ in range(H)]
h_data = []
w_data = []
for a in A:
    tmp = 0
    for w in range(W):
        tmp += a[w]
    h_data.append(tmp)
for w in range(W):
    tmp = 0
    for h in range(H):
        tmp += A[h][w]
    w_data.append(tmp)
for h in range(H):
    tmp = []
    for w in range(W):
        tmp.append(h_data[h] + w_data[w] - A[h][w])
    print(*tmp)

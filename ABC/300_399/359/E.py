N = int(input())
H = [int(l) for l in input().split()]
# 量，高さ，幅
Data = [(H[0], H[0], 1)]
idx = 0
for n in range(1, N):
    h = H[n]
    if Data[idx][1] < h:
        r, h_, we = Data[idx]
    else:
        pass

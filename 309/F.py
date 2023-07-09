N = int(input())
H = []
W = []
D = []
for n in range(N):
    tmp = [int(l) for l in input().split()]
    tmp.sort()
    h, w, d = tmp
    H.append([h, n])
    W.append([w, n])
    D.append([d, n])
H.sort()
W.sort()
D.sort()
hdat = []
wdat = []
ddat = []
for idx in range(N):
    hdat.append(H[idx][1])
    wdat.append(W[idx][1])
    ddat.append(D[idx][1])
print(hdat, wdat, ddat)

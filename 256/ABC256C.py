H1, H2, H3, W1, W2, W3 = [int(l) for l in input().split()]
H = [H1, H2, H3]
W = [W1, W2, W3]
HMax = max(H)
WMax = max(W)
for a in range(1, HMax + 1):
    for b in range(1, HMax + 1):
        for d in range(1, WMax + 1):
            for e in range(1, WMax + 1):
                c = H1 - a - b
                f = H2 - d - e
                g = W1 - a - d

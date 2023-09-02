H, W, K = [int(l) for l in input().split()]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if h * w < K:
            continue

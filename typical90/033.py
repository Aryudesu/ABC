H, W = [int(l) for l in input().split()]
print((H//2 + H % 2) * (W//2 + W % 2) if H != 1 and W != 1 else H * W)

H, W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
else:
    result = (H // 2) * W
    result += (H % 2) * (W//2 + (W % 2))
    print(result)

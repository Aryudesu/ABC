H, W = map(int, input().split())
print("#" * W)
for h in range(H-2):
    print("#", end="")
    print("." * (W-2), end="")
    print("#")
print("#" * W)

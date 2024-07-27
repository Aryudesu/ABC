H, W = [int(l) for l in input().split()]
Sy, Sx = [int(l) - 1 for l in input().split()]
C = []
for h in range(H):
    C.append([l for l in input()])
X = input()
for x in X:
    if x == "L":
        if Sx > 0 and C[Sy][Sx - 1] != "#":
            Sx -= 1
    elif x == "R":
        if Sx < W - 1 and C[Sy][Sx + 1] != "#":
            Sx += 1
    elif x == "U":
        if Sy > 0 and C[Sy - 1][Sx] != "#":
            Sy -= 1
    elif x == "D":
        if Sy < H - 1 and C[Sy + 1][Sx] != "#":
            Sy += 1
    else:
        raise Exception()
print(Sy + 1, Sx + 1)

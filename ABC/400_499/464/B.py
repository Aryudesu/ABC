H, W = map(int, input().split())
C = [input() for _ in range(H)]
while C:
    if C[0].count(".") == W:
        C.pop(0)
    else:
        break
while C:
    if C[-1].count(".") == W:
        C.pop()
    else:
        break
H = len(C)
l = 0
while l < W:
    tmp = 0
    for h in range(H):
        if C[h][l] == ".":
            tmp += 1
    if tmp == H:
        l += 1
    else:
        break
r = W-1
while l < r:
    tmp = 0
    for h in range(H):
        if C[h][r] == ".":
            tmp += 1
    if tmp == H:
        r -= 1
    else:
        break
for h in range(H):
    print(C[h][l:r+1])

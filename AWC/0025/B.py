H, W, N = map(int, input().split())
S = [input() for h in range(H)]
nimotsu = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            nimotsu.add((h, w))
T = input()
posY, posX = 0, 0
p = (posY, posX)
if p in nimotsu:
    nimotsu.discard(p)
for t in T:
    dy, dx = 0, 0
    if t == "U":
        dy -= 1
    elif t == "D":
        dy += 1
    elif t == "L":
        dx -= 1
    elif t == "R":
        dx += 1
    else:
        raise ValueError()
    posY = min(max(posY + dy, 0), H-1)
    posX = min(max(posX + dx, 0), W-1)
    p = (posY, posX)    
    if p in nimotsu:
        nimotsu.discard(p)
print(len(nimotsu))

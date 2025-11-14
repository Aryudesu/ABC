def s2t(sx, sy, tx, ty):
    for _ in range(tx - sx):
        print("R", end="")
    for _ in range(ty - sy):
        print("U", end="")

def t2s(sx, sy, tx, ty):
    for _ in range(tx - sx):
        print("L", end="")
    for _ in range(ty - sy):
        print("D", end="")

sx, sy, tx, ty = map(int, input().split())
s2t(sx, sy, tx, ty)
t2s(sx, sy, tx, ty)
print("D", end="")
s2t(sx, sy-1, tx + 1, ty)
print("LU", end="")
t2s(sx-1, sy, tx, ty+1)
print("R", end="")

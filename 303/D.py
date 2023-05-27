X, Y, Z = [int(l) for l in input().split()]
S = input()
on = Z
off = 0
for s in S:
    new_on = 0
    new_off = 0
    if s == "a":
        new_off = off + X
        if new_off > on + Z + X:
            new_off = on + Z + X
        new_on = on + Y
        if new_on > off + Z + Y:
            new_on = off + Z + Y
    elif s == "A":
        new_on = on + X
        if new_on > off + Z + X:
            new_on = off + Z + X
        new_off = off + Y
        if new_off > on + Z + Y:
            new_off = on + Z + Y
    on = new_on
    off = new_off
print(on if on < off else off)

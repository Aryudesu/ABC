Xa, Ya, Xb, Yb, Xc, Yc = [int(l) for l in input().split()]
Xa, Ya, Xb, Yb, Xc, Yc = 0, 0, Xb - Xa, Yb - Ya, Xc - Xa, Yc - Ya
if Xb < 0:
    Xb, Xc = -Xb, -Xc
if Yb < 0:
    Yb, Yc = -Yb, -Yc
if Yb == 0:
    Xb, Yb, Xc, Yc = Yb, Xb, Yc, Xc
result = 0
if Xb != 0:
    result += (Xb - 1) + (Yb - 1) + abs(Xc - Xb) + abs(Yc - Yb)
    if Xc < Xb and Yc < Yb:
        result += 5
    elif Xc == Xb or Yc == Yb:
        result += 3 if (Yc - Yb) + (Xc - Xb) < 0 else 1
    else:
        result += 3
else:
    result += Yb - 1 + abs(Xc - Xb) + abs(Yc - Yb)
    if Yc < Yb:
        result += 4
    elif Xc != Xb:
        result += 2
print(result)

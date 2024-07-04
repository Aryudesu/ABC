Sx, Sy = [int(l) for l in input().split()]
if Sy % 2 == 0 and Sx % 2 == 1:
    Sx -= 1
elif Sy % 2 == 1 and Sx % 2 == 0:
    Sx -= 1
Tx, Ty = [int(l) for l in input().split()]
if Ty % 2 == 0 and Tx % 2 == 1:
    Tx -= 1
elif Ty % 2 == 1 and Tx % 2 == 0:
    Tx -= 1
# 座標の補正
Tx, Ty = abs(Tx - Sx), abs(Ty - Sy)
Sx, Sy = 0, 0
# print(Tx, Ty, Sx, Sy)
if Ty > Tx:
    result = Ty
else:
    result = Ty + (Tx - Ty) // 2
print(result)

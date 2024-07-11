x1, y1 = [int(l) for l in input().split()]
x2, y2 = [int(l) for l in input().split()]
x3, y3 = [int(l) for l in input().split()]
param = []
if x1 == x2:
    param.append(str(x3))
elif x1 == x3:
    param.append(str(x2))
elif x2 == x3:
    param.append(str(x1))
if y1 == y2:
    param.append(str(y3))
elif y1 == y3:
    param.append(str(y2))
elif y2 == y3:
    param.append(str(y1))
print(" ".join(param))

SAB, SAC, SBC = [l for l in input().split()]
A, B, C = [0, 0, 0]
if SAB == "<":
    B += 1
else:
    A += 1
if SAC == "<":
    C += 1
else:
    A += 1
if SBC == "<":
    C += 1
else:
    B += 1
ALP = "ABC"
data = [A, B, C]
for i in range(3):
    if data[i] == 1:
        print(ALP[i])

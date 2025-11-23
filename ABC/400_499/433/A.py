X, Y, Z = map(int, input().split())

tmpA = X - Z*Y
tmpB = Z - 1

if tmpA % tmpB == 0 and tmpA >= 0:
    print("Yes")
else:
    print("No")

a, b = [int(l) for l in input().split()]
if b - a == 1:
    print("Yes")
elif b == 10 and a == 1:
    print("Yes")
else:
    print("No")

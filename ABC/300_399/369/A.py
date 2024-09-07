A, B = [int(l) for l in input().split()]
if A - B == 0:
    print(1)
elif (A - B) % 2:
    print(2)
else:
    print(3)

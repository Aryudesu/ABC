A1, A2, A3 = [int(l) for l in input().split()]
if A1 * A2 == A3 or A1 * A3 == A2 or A2 * A3 == A1:
    print("Yes")
else:
    print("No")

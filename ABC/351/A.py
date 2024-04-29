A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
SA = sum(A)
SB = sum(B)
if (SA < SB):
    print(0)
else:
    print(SA - SB + 1)

A, B, C = [int(l) for l in input().split()]
print("Yes" if A + B == C or A + C == B or B + C == A or A == B == C else "No")

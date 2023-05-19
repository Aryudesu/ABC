A, B, C, D = [int(l) for l in input().split()]
AB2 = (A + B)/2
CD2 = (C + D)/2
BA2 = (B - A)/2
DC2 = (D - C)/2
print("Yes" if abs(AB2 - CD2) <= BA2 + DC2 else "No")

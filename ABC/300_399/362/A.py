R, G, B = [int(l) for l in input().split()]
C = input()
if C == "Red":
    R *= 100
elif C == "Green":
    G *= 100
elif C == "Blue":
    B *= 100
print(min([R, G, B]))

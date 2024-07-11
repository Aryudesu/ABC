S = input()
U = 0
L = 0
for s in S:
    if s.isupper():
        U += 1
    else:
        L += 1
print(S.upper() if U > L else S.lower())


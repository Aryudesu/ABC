S = input()
T = 0
for s in S:
    T += int(s)
print("No" if int(S) % T else "Yes")

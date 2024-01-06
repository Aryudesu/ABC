P1 = {"AB", "BC", "CD", "DE", "EA"}
P2 = {"AC", "AD", "BD", "BE", "CE"}
S1 = input()
T1 = input()
S2 = S1[1] + S1[0]
T2 = T1[1] + T1[0]
if (S1 in P1 or S2 in P1) and (T1 in P1 or T2 in P1):
    print("Yes")
elif (S1 in P2 or S2 in P2) and (T1 in P2 or T2 in P2):
    print("Yes")
else:
    print("No")

def isPerfect(S):
    BList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MList = "abcdefghijklmnopqrstuvwxyz"
    Big = False
    Min = False
    if S[0] in BList:
        Big = True
    if S[0] in MList:
        Min = True
    for n in range(len(S) - 1):
        if S[n] == S[n + 1]:
            return False
        if S[n + 1] in BList:
            Big = True
        if S[n + 1] in MList:
            Min = True
    return Big and Min


S = sorted(input())
S.sort()
if isPerfect(S):
    print("Yes")
else:
    print("No")

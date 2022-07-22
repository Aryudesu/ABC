S = list(input())
S.sort()
if S[0] == S[2]:
    print("-1")
elif S[0] == S[1]:
    print(S[2])
else:
    print(S[0])

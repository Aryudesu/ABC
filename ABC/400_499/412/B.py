S = input()
T = set(list(input()))
res = True
for i in range(2, len(S)):
    if S[i].isupper() and not S[i-1] in T:
        res = False
print("Yes" if res else "No")

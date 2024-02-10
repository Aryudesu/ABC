Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dat = {a.lower():a for a in Alphabet}
S = input()
T = S
S = list(S.lower())
S[0] = dat[S[0]]
S = "".join(S)
print("Yes" if S == T else "No")

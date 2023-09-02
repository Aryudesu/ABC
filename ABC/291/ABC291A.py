S = input()
st = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for idx in range(len(S)):
    if S[idx] in st:
        print(idx + 1)

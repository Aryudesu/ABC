W = [False] * 8
H = [False] * 8
for i in range(8):
    S = input()
    for j in range(8):
        if S[j] == "#":
            H[i] = True
            W[j] = True
print(W.count(False) * H.count(False))

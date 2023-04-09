def calc(R, B, N, K, Q):
    if B[0] % 2 == B[1] % 2:
        return False
    if R[0] < K[0] and K[0] < R[1]:
        return True
    return False


S = input()
R = []
B = []
N = []
K = []
Q = []
LS = len(S)
for i in range(LS):
    if S[i] == "R":
        R.append(i)
    elif S[i] == "B":
        B.append(i)
    elif S[i] == "N":
        N.append(i)
    elif S[i] == "K":
        K.append(i)
    elif S[i] == "Q":
        Q.append(i)
print("Yes" if calc(R, B, N, K, Q) else "No")

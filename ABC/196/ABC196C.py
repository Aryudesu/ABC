S = input()
L = len(S)
N1 = int(S[:L//2])
N2 = int(S[L//2:])
if N1 > N2:
    print(N1-1)
else:
    print(N1)

def calc(N, S):
    if N >= 3:
        return not (S[0] == "A" and S[-1] == "B")
    elif N == 2:
        return S == "AA" or S == "BB"
    else:
        return True


N = int(input())
S = input()
if calc(N, S):
    print("Yes")
else:
    print("No")

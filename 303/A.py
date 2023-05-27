def is_similar(N, S, T):
    for i in range(N):
        if S[i] == T[i]:
            continue
        elif S[i] == "o" and T[i] == "0":
            continue
        elif S[i] == "0" and T[i] == "o":
            continue
        elif S[i] == "1" and T[i] == "l":
            continue
        elif S[i] == "l" and T[i] == "1":
            continue
        else:
            return False
    return True


N = int(input())
S = input()
T = input()
print("Yes" if is_similar(N, S, T) else "No")

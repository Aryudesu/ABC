def calc(N, L, R, S):
    for idx in range(L-1, R):
        if S[idx] != "o":
            return False
    return True

N, L, R = [int(l) for l in input().split()]
S = input()
print("Yes" if calc(N, L, R, S) else "No")

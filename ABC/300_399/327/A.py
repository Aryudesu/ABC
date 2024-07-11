def calc(N, S):
    for n in range(N-1):
        if S[n] == "a" and S[n+1] == "b":
            return True
        if S[n] == "b" and S[n+1] == "a":
            return True
    return False


N = int(input())
S = input()
print("Yes" if calc(N, S) else "No")

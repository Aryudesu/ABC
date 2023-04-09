def calc(N, S):
    if N == 1:
        return True
    for n in range(N - 1):
        if S[n] == S[n+1]:
            return False
    return True


N = int(input())
S = input()
print("Yes" if calc(N, S) else "No")

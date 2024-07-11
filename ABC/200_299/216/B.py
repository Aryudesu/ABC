def calc(N, S, T):
    for n in range(N - 1):
        for m in range(n + 1, N):
            if S[n] == S[m] and T[n] == T[m]:
                return True
    return False

N = int(input())
S = []
T = []
for n in range(N):
    s, t = [l for l in input().split()]
    S.append(s)
    T.append(t)
print("Yes" if calc(N, S, T) else "No")

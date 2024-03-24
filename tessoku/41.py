N, S, res = input(), input(), False
for idx in range(len(S) - 2):
    if S[idx] == S[idx+1] and S[idx+1] == S[idx+2]:
        res = True
print("Yes" if res else "No")

S = input()
N = len(S)
result = 0
for n in range(N):
    m = N - n - 1
    if S[n] == "C":
        result += min(n, m) + 1
print(result)

S = input()
N = len(S)
result = 0
for i in range(N):
    for j in range(i + 2, N):
        s = S[i:j+1]
        if s[0] == "t" and s[-1] == "t":
            num = 0
            for t in s:
                if t == "t":
                    num += 1
            result = max(result, (num - 2)/(len(s) - 2))
print(result)

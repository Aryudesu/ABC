N = int(input())
S = input()
T = input()
result = []
isOk = True
for i in range(N):
    s, t = S[i], T[i]
    if s == t:
        if s == "?":
            result.append("?")
        else:
            result.append(s)
    else:
        if s == "?":
            result.append(t)
        elif t == "?":
            result.append(s)
        else:
            result.append("!")
            isOk = False
print("".join(result))
print("Yes" if not isOk else "No")


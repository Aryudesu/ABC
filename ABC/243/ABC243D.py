N, X = input().split()
S = input()
X = list(bin(int(X)))
for s in S:
    if s == "U":
        X.pop()
    elif s == "L":
        X.append("0")
    else:
        X.append("1")
print(int("".join(X), 2))

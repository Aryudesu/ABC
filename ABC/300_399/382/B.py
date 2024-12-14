N, D = [int(l) for l in input().split()]
S = input()
ck = S.count("@") - D
c = 0
result = []
for s in S:
    if s == ".":
        result.append(s)
    else:
        result.append("@" if c < ck else ".")
        c += 1
print("".join(result))

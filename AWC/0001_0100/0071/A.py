S = input()
c = 0
result = []
for s in S:
    if s == "(":
        c += 1
    else:
        c -= 1
    result.append(c)
print(max(result))

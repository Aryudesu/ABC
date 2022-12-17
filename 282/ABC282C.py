N = int(input())
S = input()
f = False
result = []
for s in S:
    if s == '"':
        f = not f
    if not f and s == ",":
        result.append(".")
    else:
        result.append(s)
print("".join(result))
